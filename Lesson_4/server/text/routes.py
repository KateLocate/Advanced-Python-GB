from .controllers import *

routes = [
    {'action': 'upper_text',
     'controller': get_upper_text},
    {'action': 'get_time',
     'controller': get_time},
    {'action': 'lower_text',
     'controller': get_lower_text}
]