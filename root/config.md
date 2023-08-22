# ENVIRONMENT VAR*

ENVIRONMENT=local
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_HOST=localhost
DB_USER=thestaffmanagerdbrootuser
DB_PASS=thestaffmanagerdbrootuserpassword
DB_NAME=thestaffmanagerdb
DB_PORT=django.db.backends.postgresql_psycopg2
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@server.com
EMAIL_HOST_PASSWORD=youremailpassword
EMAIL_PORT=587
BASE_URL=http://127.0.0.1:8000
DEFAULT_FROM_EMAIL=Support-Team <youremail@server.com>
DEBUG=True
SECRET_KEY=YUwsjlxk30PYf6dovmiUK8c0i1MARKIiejYh7kSDv3fiBq2mlWmeXap
TIME_ZONE=Asia/Karachi
GOOGLE_CALLBACK_URL=http://127.0.0.1:8000/accounts/google/login/callback/
ALLOWED_HOST=127.0.0.1
SITE_ID=1
DOMAIN=127.0.0.1:8000
USE_SSL=True

# MIGRATIONS
make sure to follow this migrations order.
1. core
2. users
3. ...

# MISSING
accounts templates are missing