# Python SQLAlchemy Example

### Connect to Postgres
```shell
# Connect to the database
# docker exec -ti {container} psql -U {user} {database}
docker exec -ti sql-alchemy-postgres psql -U user1 tutorial

# Connect to postgres (standard way)
psql -U postgres -W -p 5432 -h localhost

# Connect to container with a specific user
docker exec -it -u {user} {container} bash
docker exec -it -u postgres sql-alchemy-postgres bash
docker exec -it -u root sql-alchemy-postgres bash
```


### PgAdmin Config

```shell
# http://localhost:3001
Register -> Server
General:
  Name: Any name
Connection:
  Host name/address: postgres # docker service name
  Username: user1
  Password: pass1
```
