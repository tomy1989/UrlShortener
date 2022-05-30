### Features

- Creating shortlink from full link
- Save to db + amout of clicks
- Redirect to full link using shortlink
- Python django
- Postman https://documenter.getpostman.com/view/15932641/Uz5CNebM

# URL shortener

![](https://lh3.googleusercontent.com/GiRiQRLCt0HvR2WuLlLUhvQS-_AxCOuoKmB11b-VTmyGjlJtL_6iyaCuL0xCp1SDwSM)

![](https://img.shields.io/badge/-tomy%20poliakov-orange) ![](https://img.shields.io/pypi/pyversions/django)


**Table of Contents**

+ [Features](#features)
- [Configure backend (Django)](#configure-backend--django)
- [Some usefull information](#some-usefull-information)
- [End](#end)

# configure-backend--django
Configure backend (Django)
====
Backend files you can find in /APi

Make sure you have **python3.9+** installed

Python installation you can find [here](https://www.python.org/downloads/)


venv folder = enviroment that have been used
turn on enviroment when in folder API (not must)
```
venv\Scripts\activate
```
In API/api can find file req.txt

Make sure you have pip installed
can use this command to install all needed packages:
#### Pip install from requirements file, code

`$ pip install -r /path/to/requirements.txt`

 if you not have pip installed you can follow instuction [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) for installing

#### Run django server
```python
python manage.py runserver
```

### Some usefull information
Simple basic url shortener

For using any other db inside UrlShortener settings.py in DATABASES
feel free to configure a new db if want.

this projet not contains any front or visualy testing only backend

for testing can use postman, curl or any other tool
added bat files, run curl commands

any click on shortlink amout of clicks increase(not 1 click for 1 user, user can access link many times and the counter will increase)
i not sure if I should to handle 1 click per user in this assigment, for doing it i probably added track in db on users clicked it

Inside TESTS folder can find bat files, run curl commands in different situations
### End