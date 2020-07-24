import os
from datetime import timedelta

getenv = os.environ.get

# DB config
{%- if cookiecutter.database == "sqlite" %}
DEFAULT_DBURI = "sqlite:///{{cookiecutter.app_slug}}.db"
{%- elif cookiecutter.database == "postgres" %}
DB_USER = "{{cookiecutter.db_user}}"
DB_PASSWD = "{{cookiecutter.db_passwd}}"
DB_IPADDR = "{{cookiecutter.db_addr}}"
DB_NAME = "{{cookiecutter.db_name}}"
DEFAULT_DBURI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_IPADDR}/{DB_NAME}'
{%- endif %}

class Config(object):
    """Base configuration."""

    SECRET = getenv('SECRET', 'secret')
    DATABASE_URI = getenv('DATABASE_URI', DEFAULT_DBURI)


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    TESTING = False
