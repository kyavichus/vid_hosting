"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application

site.addsitedir('/media/sde/vovideo/venv/lib/python3.9/site-packages')
sys.path.append('/media/sde/vovideo/vid_hosting')
sys.path.append('/media/sde/vovideo/vid_hosting/config')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Activate your virtual env
#activate_env=os.path.expanduser('/media/sde/vovideo/venv/bin/activate')
#exec(open(activate_env).read(), {'__file__': activate_env})

application = get_wsgi_application()
