Welcome
===

First of all, this is nothing but an ever changing playground for me to test things Docker/Deployment related. You're welcomed to see as my repository evolves from what is a blank slate to a fully functional deployment


Quickstart
===

Since you're here, just go ahead and `docker-compose up --build`.


# Docker Compose version: 3.3

.env
===
```
# ATTENTION -------------------------------------------------
# These are the default ENVIRONMENT variables that
# will be used during the default start up of the application

# NGINX -----------------------------------------------------
NGINX_LISTEN_PORT=8001

# POSTGRES --------------------------------------------------
POSTGRES_LISTEN_PORT=54321
POSTGRES_DB=ouchinsurance
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# APP SETTINGS ----------------------------------------------
DATABASE_NAME=ouchinsurance
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
DATABASE_ATOMIC_REQUESTS=1
```
