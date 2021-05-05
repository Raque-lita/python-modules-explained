# this is the `app` module

# importing from the `app.utils` module
from app.utils import some_utility

# importing from `app.models` module
from app.models import MyModel, my_model_factory

# Importing from the `app.models.another_model` module...
# because I haven't imported `AnotherModel` into the `__init__.py` in `models`
# I'm not able to access `AnotherModel` from there, so I have to go all the way
# to the `another_model` module to get it
from app.models.another_model import AnotherModel

def run_app():
	# do some thing to run the app
	...
