Welcome
===

First of all, this is nothing but an ever changing playground for me to test things Docker/Deployment related. You're welcomed to see as my repository evolves from what is a blank slate to a fully functional deployment


Quickstart
===
```bash
$ docker-compose up --build
```

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


ACME Challenge for LetsEncrypt
=====
For the ACME challenge for LetsEncrypt, this should be done on a remote server only. Ensure that the external port that is exposed for listening with Nginx is set to 80. Then `sudo ./init-letsencrypt.sh` and look at it go.


Personalization
=====
You can make a copy of the `.env` file and source it before you run the `docker-compose` command. Same goes for the `docker-compose.yaml` where you can `docker-compose -f <a_copy_of_the_file>.yaml`.
