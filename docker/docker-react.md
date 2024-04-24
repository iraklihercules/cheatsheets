# Docker React

### 1. Docker Infrastructure

docker-compose.yaml
```yaml
version: "3.9"

services:
  app:
    build: ./app
    container_name: react-app
#    command: tail -f /dev/null  # Keeps the container running without rebuilding process.
    ports:
      - 8000:8080
    volumes:
      - ./app/src:/app
      - /app/node_modules  # Required to keep modules
    networks:
      - react

networks:
  react:
    driver: bridge
```

app/Dockerfile
```Dockerfile
FROM node:21

USER root

RUN echo 'alias ll="ls -al"' >> /root/.bashrc \
    && echo 'alias ll="ls -al"' >> /home/node/.bashrc

RUN npm install -g vite
EXPOSE 8080

USER node
WORKDIR /app

COPY --chown=node:node src/package.json /app/
COPY --chown=node:node src/package-lock.json /app/
RUN npm install

COPY --chown=node:node src/ .

CMD ["npm", "run", "dev"]
```

Makefile
```Makefile
.PHONY:
start:
	docker compose up -d

.PHONY:
stop:
	docker compose stop

.PHONY:
reload:
	docker compose down
	docker compose build
	docker compose up -d

.PHONY:
shell:
	docker exec -it -u node react-app bash
```

### 2. Project Setup

1. Create new project
```bash
$ npm create vite@latest
# project name: . (current directory)
# Choose React
# Choose TypeScript
```

2. In the package.json specify the port
```json
{
  "scripts": {
    "dev": "vite --port 8080 --host"
  }
}
```
