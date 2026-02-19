#concept #docker #networking #february2026

# How Docker Networking Works

## What is it?
Docker networking is how containers communicate with each other, with the host machine, and with the outside world. Docker creates virtual networks and uses Linux network primitives (bridges, veth pairs, iptables rules) under the hood to route traffic between containers.

## Why does it matter?
Every real application has multiple parts that need to talk to each other — an API talks to a database, a frontend talks to an API. In Docker, each container is isolated by default. Without understanding networking, your containers will be lonely islands that can't reach anything. You need networking to:
- Expose your app to the browser (port mapping)
- Let a backend container reach a database container
- Keep internal services hidden from the outside world

## How it works

Docker has four main network drivers:

### 1. Bridge (default)
When you run a container without specifying a network, Docker connects it to a **bridge network** called `bridge`.

Think of it like a virtual switch inside your machine. All containers on the same bridge can talk to each other using their IP addresses.

```
  Host Machine
  ┌───────────────────────────────┐
  │        docker0 (bridge)       │
  │       ┌───────────────┐       │
  │       │  172.17.0.1   │       │
  │       └──┬─────────┬──┘       │
  │          │         │          │
  │   ┌──────┴──┐ ┌───┴──────┐   │
  │   │ Container│ │ Container│   │
  │   │ 172.17.0.2│ │ 172.17.0.3│   │
  │   └─────────┘ └──────────┘   │
  └───────────────────────────────┘
```

- `docker0` is a Linux bridge device created by Docker
- Each container gets a **veth pair** (virtual ethernet cable): one end inside the container, one end attached to the bridge
- Containers on the default bridge can reach each other by IP but **not by container name**

### 2. User-defined bridge (recommended)
Created with `docker network create`. Works like the default bridge but with important improvements:

```bash
# create a custom network
docker network create my-network

# run containers on that network
docker run -d --name api --network my-network flask-api:v1
docker run -d --name db --network my-network postgres:16
```

Key difference: containers on a user-defined bridge can reach each other **by name**. The `api` container can connect to `db:5432` instead of needing to know the IP address. Docker runs an internal DNS server that resolves container names.

### 3. Host
The container shares the host's network stack directly. No isolation, no port mapping needed.

```bash
docker run --network host flask-api:v1
```

- The app inside listens on port 5000 → it's immediately on `localhost:5000` on the host
- Fast (no NAT overhead) but no network isolation
- Useful for performance-sensitive or monitoring tools

### 4. None
No networking at all. The container is completely isolated.

```bash
docker run --network none alpine
```

Rarely used, but useful for batch jobs that don't need network access.

## Practical example

A common pattern: API + Database on a custom network.

```bash
# create the network
docker network create app-net

# run postgres on that network
docker run -d \
  --name db \
  --network app-net \
  -e POSTGRES_PASSWORD=secret \
  postgres:16

# run the API on the same network
# notice: the API connects to "db" by name, not by IP
docker run -d \
  --name api \
  --network app-net \
  -p 8080:5000 \
  -e DATABASE_HOST=db \
  -e DATABASE_PORT=5432 \
  flask-api:v1

# only the API is exposed to the host (port 8080)
# the database is only reachable from within app-net
```

Inspect the network to see connected containers:

```bash
docker network inspect app-net
```

## Port mapping explained

`-p 8080:5000` means: "traffic arriving at host port 8080 gets forwarded to container port 5000."

```
 Outside world
      │
      ▼
 Host port 8080  ──(iptables NAT rule)──►  Container port 5000
```

Docker creates iptables rules automatically to handle this forwarding. You can see them with:

```bash
sudo iptables -t nat -L -n
```

## Common mistakes / gotchas

- **Using the default bridge for multi-container apps**: containers can't resolve each other by name on the default bridge. Always create a custom network with `docker network create`.
- **Forgetting `-p` and wondering why you can't reach the container**: without port mapping, the container's ports are only accessible from other containers on the same network, not from the host.
- **Using `localhost` in the app to reach another container**: inside a container, `localhost` is the container itself. Use the other container's name (e.g., `db`) instead.
- **Port conflicts**: if host port 8080 is already in use, `docker run -p 8080:5000` will fail. Use `docker ps` or `ss -tlnp` to check what's using a port.

## Related concepts
- [[How Linux Works, Chapter 1]] — Linux layers (networking happens at kernel level)
- [[Networking in Linux]] — the underlying Linux network commands
- [[Creating a container like from scratch using Fedora]] — Step 4 covers network namespaces manually, which is exactly what Docker automates
