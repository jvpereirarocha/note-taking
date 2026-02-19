#project #docker #python #february2026

# Containerizing a Python API with Docker

## Goal
Build a simple REST API with Python (Flask), containerize it with Docker, and run it with environment-based configuration.

## Tech Stack
- **Python 3.12**: application runtime
- **Flask 3.x**: lightweight web framework for the API
- **Docker**: containerization
- **curl**: testing the API endpoints

## Prerequisites
- Docker installed and running (`systemctl status docker`)
- Basic understanding of Python (just enough to read the code)
- Terminal basics (cd, ls, cat, vim)

## Architecture

```
[curl / Browser] --> [Docker Container :5000] --> [Flask API]
                            |
                     (environment variables
                      configure the app)
```

## Step-by-step

### Step 1 — Create the project structure

We need a minimal Flask app with its dependencies listed.

```bash
# create project directory
mkdir ~/flask-docker-lab && cd ~/flask-docker-lab

# create the application file
touch app.py requirements.txt Dockerfile .dockerignore
```

**Checkpoint**: Run `ls` and confirm you see all four files.

### Step 2 — Write the Flask API

A minimal API with two endpoints: a health check and a greeting.

```python
# app.py
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read configuration from environment variables
APP_ENV = os.getenv("APP_ENV", "development")
APP_PORT = int(os.getenv("APP_PORT", 5000))

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "environment": APP_ENV})

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello, {name}!", "environment": APP_ENV})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
```

Key details:
- `os.getenv("APP_ENV", "development")` reads env vars with a default fallback. This is how real apps are configured in containers.
- `host="0.0.0.0"` is important. Without it, Flask only listens on `127.0.0.1` and the container won't accept external connections.

```
# requirements.txt
flask==3.1.1
```

**Checkpoint**: Run locally to make sure it works before containerizing.

```bash
pip install -r requirements.txt
python app.py
# In another terminal:
curl http://localhost:5000/health
# Expected: {"environment":"development","status":"healthy"}
```

### Step 3 — Write the Dockerfile

This is where we tell Docker how to build our image.

```dockerfile
# Dockerfile

# Start from a slim Python image (smaller = faster builds, less attack surface)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (Docker layer caching optimization)
# If requirements.txt doesn't change, Docker reuses the cached pip install layer
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application code
COPY . .

# Document which port the app uses (informational, doesn't actually publish)
EXPOSE 5000

# Command to run when the container starts
CMD ["python", "app.py"]
```

Why copy `requirements.txt` before the rest of the code:
- Docker builds images in layers. Each instruction creates a layer.
- If a layer hasn't changed, Docker reuses it from cache.
- By copying requirements first and installing dependencies, we only re-install packages when `requirements.txt` changes — not every time we edit `app.py`.

Also add a `.dockerignore` to keep the image clean:

```
# .dockerignore
__pycache__
*.pyc
.git
.env
venv/
```

**Checkpoint**: The Dockerfile should be readable and make sense top to bottom.

### Step 4 — Build the Docker image

```bash
# build the image and tag it as "flask-api:v1"
docker build -t flask-api:v1 .
```

- `-t flask-api:v1` — tags the image with a name and version
- `.` — build context is the current directory (Docker sends these files to the daemon)

Watch the output. You'll see each layer being built.

**Checkpoint**: Verify the image exists.

```bash
docker images | grep flask-api
# Expected: flask-api   v1   <image-id>   <date>   <size>
```

### Step 5 — Run the container

```bash
# run the container
docker run -d \
  --name my-api \
  -p 8080:5000 \
  -e APP_ENV=production \
  flask-api:v1
```

- `-d` — run in detached mode (background)
- `--name my-api` — give the container a human-readable name
- `-p 8080:5000` — map host port 8080 to container port 5000
- `-e APP_ENV=production` — set an environment variable inside the container

**Checkpoint**: Test the running container.

```bash
# check the container is running
docker ps

# test the health endpoint (note: port 8080 on the host)
curl http://localhost:8080/health
# Expected: {"environment":"production","status":"healthy"}

# test the greeting endpoint
curl http://localhost:8080/hello/jvictor
# Expected: {"message":"Hello, jvictor!","environment":"production"}

# check the container logs
docker logs my-api
```

### Step 6 — Inspect and debug the container

Learning how to look inside a running container is essential for debugging.

```bash
# open a shell inside the running container
docker exec -it my-api /bin/bash

# once inside, you can inspect:
env              # see all environment variables
ls /app          # see the application files
cat /etc/os-release  # see the base OS (Debian slim)
ps aux           # see running processes
exit             # leave the container
```

- `docker exec -it` — execute an interactive (`-i`) terminal (`-t`) session in a running container
- This is the equivalent of SSH-ing into a server, but for containers

**Checkpoint**: You should see `APP_ENV=production` in the `env` output.

### Step 7 — Clean up

```bash
# stop the container
docker stop my-api

# remove the container
docker rm my-api

# (optional) remove the image
docker rmi flask-api:v1
```

## Problems I Hit

### Problem 1: "Connection refused" when curling the container
- **Symptom**: `curl http://localhost:8080/health` returned "Connection refused"
- **Cause**: Flask was running on `127.0.0.1` (localhost inside the container), which is not accessible from outside the container
- **Fix**: Changed `app.run()` to `app.run(host="0.0.0.0")` so Flask listens on all interfaces
- **Lesson**: Inside a container, `127.0.0.1` means the container's own loopback. To accept connections from outside (including port-mapped traffic from the host), the app must bind to `0.0.0.0`

### Problem 2: Code changes not showing up after rebuilding
- **Symptom**: Edited `app.py`, rebuilt the image, but the old response still appeared
- **Cause**: Docker was using a cached layer. Since `COPY . .` came after `RUN pip install`, and pip install layer was cached, Docker thought nothing changed
- **Fix**: Ran `docker build --no-cache -t flask-api:v1 .` to force a fresh build. Alternatively, the layer ordering in our Dockerfile should handle this correctly — double-checked and the issue was actually that I forgot to stop/remove the old container before starting a new one with the same name
- **Lesson**: Always `docker stop` + `docker rm` the old container before running a new one with the same `--name`. Or use `docker run --rm` to auto-remove on stop.

## Key Takeaways

- **Environment variables are the standard way to configure containers**. Hardcoding values is an anti-pattern. The same image should work in dev, staging, and production — only the env vars change.
- **Layer ordering in Dockerfiles matters for build speed**. Put things that change rarely (dependencies) before things that change often (source code).
- **`0.0.0.0` is not optional in containers**. Apps must listen on all interfaces, not just localhost.
- **`docker exec` is your debugging best friend**. When something goes wrong, jump inside the container and inspect.
- **Containers are ephemeral**. When you stop and remove a container, everything inside it is gone. That's why volumes exist — for data that must persist.

## Commands Cheat Sheet

| Command                                          | What it does                            |
| ------------------------------------------------ | --------------------------------------- |
| `docker build -t name:tag .`                     | Build an image from a Dockerfile        |
| `docker run -d --name x -p host:container image` | Run a container in the background       |
| `docker ps`                                      | List running containers                 |
| `docker ps -a`                                   | List all containers (including stopped) |
| `docker logs <name>`                             | Show container stdout/stderr            |
| `docker exec -it <name> /bin/bash`               | Open a shell inside a container         |
| `docker stop <name>`                             | Stop a running container                |
| `docker rm <name>`                               | Remove a stopped container              |
| `docker images`                                  | List local images                       |
| `docker rmi <image>`                             | Remove an image                         |
|                                                  |                                         |

## References
- Flask documentation: https://flask.palletsprojects.com
- Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- Docker CLI reference: https://docs.docker.com/reference/cli/docker/
