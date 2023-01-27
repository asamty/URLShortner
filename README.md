# URL shortner application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/asamty/URLShortner.git
$ cd URLShortner
```

Create a virtual environment to install dependencies in and activate it:

1st method (Linux):

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

2nd method (Windows):

```sh
$ python -m venv env
$ env/Scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
Then, run a server:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Statistics for specific URL

Navigate to `http://127.0.0.1:8000/counter/<short_code>` in order to get access to statistics of redirects

## Statistics for all URLs can be accessed in Admin panel (http://127.0.0.1:8000/admin)


