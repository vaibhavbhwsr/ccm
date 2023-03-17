'''
Configure this file according:
MODE in settings.ini:
- dev: Development
- prod: Production
- test: Testing (not implemented yet)
'''
from .base import *                                 # noqa: F403
from decouple import config

MODE = config("MODE", default='prod')

if MODE == 'dev':
    from .dev import *                              # noqa: F403
elif MODE == 'prod':
    from .prod import *                             # noqa: F403
