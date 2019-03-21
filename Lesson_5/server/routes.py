from importlib import __import__
from functools import reduce
from settings import INSTALLED_MODULES


def get_server_routes():
    server_routes = reduce(lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(lambda submodules, module: submodules + [getattr(module, 'routes', [])],
            reduce (lambda modules, module: modules + [__import__(f'{module}.routes')],
                INSTALLED_MODULES,[]),
            []),
        [])
    return server_routes


def resolve(action, routes=None):
    routes_mapping = {route['action']: route['controller'] for route in routes
                      or get_server_routes()}
    return routes_mapping.get(action, None)
