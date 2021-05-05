# this module corresponds to the `app.models` import

from .my_model import MyModel

# because I've imported `MyModel` from `.my_model` here, now I am able to import `MyModel` directly from `app.models` instead of having to go to `app.models.my_model`.
# I've essentially turned the `models` folder into a Python module by adding the `__init__.py` file.

def my_model_factory():
	return MyModel()
