# pm64openworldrandomizer_website

**Running the Webserver**
Install python 3.11 and pipenv to easily install all the python dependencies:
```
> pip install pipenv
> pipenv install
```
Then, start a virtual environment and start the server with the following commands:

*Windows*
```
> pipenv shell
> $env:FLASK_APP = "main.py" #once per terminal only
> flask run
```

*Unix*
```
> pipenv shell
> export FLASK_APP = "main.py" #once per terminal only
> flask run
```
