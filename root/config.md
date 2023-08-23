## ENVIRONMENT VAR*
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
## TEST CREDENTIALS
### EMAIL SMTP
**EMAIL_HOST_USER**=donald.duck0762@gmail.com                           <br>
**EMAIL_HOST_PASSWORD**=bxlshrmgvwhvaave

### STRIPE
**STRIPE_PUBLIC_KEY**=pk_test_51KNUx8GWh1G1v77h4cAKDbEvH3wEbK4yVZfSGKT5f5wgShK8cipV0ctpNrZ2tqt63fsVmJp4s>  <br>
**STRIPE_SECRET_KEY**=sk_test_51KNUx8GWh1G1v77hDR40VBVDDZTK2pgUZMk0yxDyN4evl4lBg2LyxFyOQCDoLQWhgy1t9bAzc>  <br>
**STRIPE_WEBHOOK_SECRET**=whsec_1d8d3fe0a2aa5e4636cd1343c86fdc72d962593725e8d3a4ab8ad122b8522893

## MIGRATIONS
make sure to follow this migrations order.
1. core
2. users
3. ...

## MISSING
accounts templates are missing