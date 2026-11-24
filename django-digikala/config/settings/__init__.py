import os 
environment = os.getenv('DJANGO_ENV','dev').lower()

if environment == 'prod' : 
    from .prod import *
if environment == 'dev':
    from .dev import *