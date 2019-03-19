import os
from importlib import __import__
from functools import reduce


def get_server_routes():
    return reduce(
        lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(lambda modules, dir: modules + [__import__(f'{dir}.routes')],
               filter(lambda itm: os.path.isdir(itm) and itm != '__pycache__', os.listdir()), []
               ), []
    )
