# ENVIRONMENT VAR*

````
DEBUG=True
ENVIRONMENT=local
SITE_ID=1
PROTOCOL=http
DOMAIN=127.0.0.1:8000
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=db
DB_USER=dbuser
DB_HOST=localhost
DB_PASS=dbuserpassword
DB_PORT=
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@server.com
EMAIL_HOST_PASSWORD=youremailpassword
EMAIL_PORT=587
DEFAULT_FROM_EMAIL=Support-Team <youremail@server.com>
SECRET_KEY=YUwsjlxk30PYf6dovmiUK8c0i1MARKIiejYh7kSDv3fiBq2mlWmeXap
TIME_ZONE=Asia/Karachi
````


# MIGRATIONS
make sure to follow this migrations order.
1. core
2. users
3. ...

# MISSING
accounts templates are missing