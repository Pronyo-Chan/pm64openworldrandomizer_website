# pm64openworldrandomizer_website

**Running the Webserver**
Install python 3.11 and pipenv to easily install all the python dependencies:
```
> pip install pipenv
> pipenv install
```
Then, start a virtual environment and start the server with the following commands:

```
> poetry shell
> $env:FLASK_APP = "main.py" #once per terminal only
> flask run
```
**Setting up the database and storage**
This project entirely relies on a firestore db and google cloud storage, if you want to actually run it locally
you would need a service_account.json key in the root folder, linked to a google cloud account setup with the proper infrastructure.

I'm making it open source so the code is visible, not really for local development/testing from the community.

**Deploying to Google Cloud**
Don't forget to run this command to export packages to requirements.txt
> poetry export -f requirements.txt --output requirements.txt --without-hashes

**Running the Webserver**
```
> poetry shell
> $env:FLASK_APP = "main.py" #once per terminal only
> flask run
```
