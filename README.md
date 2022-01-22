# pm64openworldrandomizer_website

**Setup Instructions**
```
> pip install poetry
> poetry install
```

**Running the Webserver**
```
> poetry shell
> python manage.py runserver 0.0.0.0:8000
```

Browswing to `http://127.0.0.1:8000/` will display the Django REST Framework page, where you can POST a JSON object containing information for randomization settings. An example of a valid JSON setting is in `./randomizer/models.py`.
