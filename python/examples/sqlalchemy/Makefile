.PHONY:
start:
	docker compose up -d && docker compose logs -f

.PHONY:
stop:
	docker compose stop

.PHONY:
shell:
	docker exec -it -u 1000:1000 sql-alchemy-app bash

.PHONY:
shell-root:
	docker exec -it sql-alchemy-app bash

.PHONY:
db-shell:
	docker exec -it sql-alchemy-postgres psql -U user1 tutorial
