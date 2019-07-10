Welcome
===

First of all, this is nothing but an ever changing playground for me to test things Docker/Deployment related. You're welcomed to see as my repository evolves from what is a blank slate to a fully functional deployment


Quickstart
===

Since you're here, just go ahead and `docker-compose up --build`.

`nginx` will be started with it's barebones configuration that would not be serving your site. A new volume should be created at `/volumes/nginx/conf.d/` which is mounted to `/etc/nginx/conf.d/` in the container. You may start adding files into here, like the default `services/nginx/site.conf` and run `docker-compose nginx restart` whenever a change has been made.

Technologies
===
* Docker (Compose version: 3.3)
* Python 3.7, Django 2.3.3, Gunicorn 19.9
* Nginx
* PostgreSQL

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
