# pm64openworldrandomizer_website

**Setup Instructions**
```
> pip install poetry
> poetry install
```

**Setting up the database** **DEPRECATED, NEED UPDATE**
Local DB: 
-Install postgresql on your system
-Run the psql setup with defaults
-When asked for passwords, user papersuper, and default postgres for user. If you set it up with different user/pass, must change it in settings.py
-At the top of settings.py, change use_local_db to True

Remote DB: You need to connect to google cloud via proxy, ask Pronyo, you will need authentication
- Setup google cloud proxy and run ./cloud_sql_proxy -instances="paper-mario-randomizer-server:us-east1:paper-rando-ogre-sql"=tcp:5432
- This won't work if you have postgresql running already. On Windows, open services.msc, look for it and stop the service

**Deploying to Google Cloud**
Don't forget to run this command to export packages to requirements.txt
> poetry export -f requirements.txt --output requirements.txt --without-hashes

**Running the Webserver**
```
> poetry shell
>$env:FLASK_APP = "main.py" #first time only
> flask run
```
