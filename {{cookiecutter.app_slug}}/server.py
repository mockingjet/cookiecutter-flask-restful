import sys
sys.dont_write_bytecode = True

from flask.helpers import get_debug_flag

from {{cookiecutter.app_slug}}.app import create_app
from {{cookiecutter.app_slug}}.settings import DevConfig, ProdConfig

config = DevConfig if get_debug_flag() else ProdConfig

app = create_app(config)
