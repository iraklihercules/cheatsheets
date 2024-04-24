# Docker Python

docker-compose.yaml
```yaml
version: "3.9"

services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
      args:
        NON_PRIVILEGED_USER_NAME: developer
    container_name: python-app
    volumes:
      - ./app/src:/app

networks:
  python:
    driver: bridge
```

Dockerfile
```Dockerfile
FROM python:3.10

ARG NON_PRIVILEGED_USER_NAME="superstar"

RUN apt update

RUN groupadd --gid 1000 ${NON_PRIVILEGED_USER_NAME} \
    && useradd ${NON_PRIVILEGED_USER_NAME} --create-home --uid 1000 --gid 1000 --shell /bin/bash \
    && usermod --append --groups www-data ${NON_PRIVILEGED_USER_NAME} \
    && echo 'alias ll="ls -al"' >> /root/.bashrc \
    && echo 'alias ll="ls -al"' >> /home/${NON_PRIVILEGED_USER_NAME}/.bashrc

COPY src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
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
	docker exec -it -u 1000:1000 python-app bash

.PHONY:
shell-root:
	docker exec -it -u root python-app bash
```
