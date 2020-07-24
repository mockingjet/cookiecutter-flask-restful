# {{cookiecutter.app_name}}

> {{cookiecutter.app_short_description}}


## Installation

> Please ensure you have pipenv tool

> Or you should: pip install pipenv

```bash
# For production
$ python setup.py install

# For development
$ python setup.py develop
```

## Start Running
```bash
$ export flask_app=server.py

# migrate and upgrade for first running
$ flask db migrate
$ flask db upgrade

# For development
$ flask run

# For production
$ gunicorn -w 4 server:app
```

## Testing

```bash
$ export flask_app=server.py

# no coverage report
$ flask test

# with coverage report
$ python -m pytest tests -v --cov={{cookiecutter.app_slug}}
```