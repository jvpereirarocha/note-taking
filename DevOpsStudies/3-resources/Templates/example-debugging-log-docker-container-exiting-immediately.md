#debugging #docker #february2026

# Debugging: Docker Container Exits Immediately After Starting

## Context
I was working on the Flask API Docker project. After building the image and running the container, it showed up in `docker ps -a` as "Exited (1)" instead of staying running. The container started and died instantly.

## Symptom
```bash
$ docker run -d --name my-api -p 8080:5000 flask-api:v1
a4f8b2c1d3e5...

$ docker ps
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
# empty — nothing running

$ docker ps -a
CONTAINER ID   IMAGE          COMMAND           CREATED         STATUS                     NAMES
a4f8b2c1d3e5   flask-api:v1   "python app.py"   5 seconds ago   Exited (1) 3 seconds ago   my-api
```

The container starts and immediately exits with code 1 (general error).

## Investigation

### Attempt 1: Check the container logs
The first thing to do when a container dies is read its logs.

```bash
$ docker logs my-api
Traceback (most recent call last):
  File "/app/app.py", line 2, in <module>
    from flask import Flask, jsonify
ModuleNotFoundError: No module named 'flask'
```

**Result**: The error is clear — Flask is not installed inside the container. But I have `pip install` in my Dockerfile. Why didn't it work?

### Attempt 2: Check the Dockerfile
I re-read my Dockerfile:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

**Result**: Found it. `COPY . .` copies everything **including** `requirements.txt`, but the `COPY` and `RUN pip install` order looks correct. Let me check the build output more carefully.

### Attempt 3: Rebuild and read the build output carefully

```bash
$ docker build -t flask-api:v1 .
...
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Using cache
...
```

**Result**: Docker used a **cached layer** for the pip install step. The cache was from a previous build where `requirements.txt` was empty (I had created the file with `touch` before writing to it). Docker saw that the `COPY . .` layer hadn't changed (same files) so it reused the old pip install result — which installed nothing.

### Attempt 4 (the fix): Rebuild without cache

```bash
# remove the old container first
$ docker rm my-api

# rebuild without cache
$ docker build --no-cache -t flask-api:v1 .
...
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
Collecting flask==3.1.1
  Downloading Flask-3.1.1-py3-none-any.whl (103 kB)
...
Successfully installed flask-3.1.1 ...

# run again
$ docker run -d --name my-api -p 8080:5000 flask-api:v1

$ docker ps
CONTAINER ID   IMAGE          COMMAND           CREATED        STATUS        PORTS                    NAMES
b7e9a1c3f5d2   flask-api:v1   "python app.py"   2 seconds ago  Up 1 second   0.0.0.0:8080->5000/tcp   my-api

$ curl http://localhost:8080/health
{"environment":"development","status":"healthy"}
```

**Result**: It works. Flask is now installed correctly and the container stays running.

## Root cause
Docker's layer caching caused a stale `pip install` layer to be reused. The first time I built the image, `requirements.txt` was empty (I created it with `touch` and forgot to add `flask` before building). When I later added `flask==3.1.1` to `requirements.txt` and rebuilt, Docker saw the same `COPY . .` instruction and assumed nothing changed — it didn't detect that the *content* of a copied file had changed because the intermediate layer hash didn't change the way I expected.

The deeper fix is to restructure the Dockerfile to copy `requirements.txt` separately before copying the rest of the code:

```dockerfile
FROM python:3.12-slim
WORKDIR /app

# Copy requirements FIRST (this layer changes only when dependencies change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code AFTER (this layer changes on every code edit)
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

This way, Docker correctly invalidates the pip install cache whenever `requirements.txt` changes, because it's in its own `COPY` layer.

## Lesson learned

1. **Always check `docker logs <container>` first** when a container exits unexpectedly. The answer is almost always in the logs.
2. **Docker layer caching can serve stale results**. When in doubt, use `--no-cache` to rebuild fresh.
3. **Separate dependency installation from code copying in Dockerfiles**. Copy the dependency file (`requirements.txt`, `package.json`, `go.mod`) first, install, then copy the source code. This makes caching work correctly and also makes builds faster during development.
4. **`docker ps` only shows running containers**. Always use `docker ps -a` to see exited containers too. An exited container still has logs you can read.

## Quick debugging checklist for "container exits immediately"

For future reference, when a container dies on start:

1. `docker logs <name>` — read the error
2. `docker inspect <name>` — check exit code, environment, config
3. `docker run -it <image> /bin/bash` — start the container interactively to poke around
4. Check if the CMD/ENTRYPOINT process requires something that isn't in the image (missing dependency, missing config file, missing env var)
5. Check if the process needs to run in the foreground (some apps daemonize by default and the container exits because PID 1 finishes)
