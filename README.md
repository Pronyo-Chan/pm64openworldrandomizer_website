# pm64openworldrandomizer_website

**Setup Instructions**
```
> pip install poetry
> poetry install
```

**Setting up the database and storage**
Local DB: 
You can test with the dev environment db/storage by having the json key in the project's root folder (Ask Pronyo)
Else, it's possible to set a local DB but not storage afaik. Just use dev but don't spam because egress data (that comes out of the cloud)
is billed (altough very little)

**Deploying to Google Cloud**
Don't forget to run this command to export packages to requirements.txt
> poetry export -f requirements.txt --output requirements.txt --without-hashes

**Running the Webserver**
```
> poetry shell
> $env:FLASK_APP = "main.py" #once per terminal only
> flask run
```
