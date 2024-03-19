import sys
import os

project_path = "/usr/home/kuba04500/domains/danews.pl/public_python"
sys.path.append(project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'news.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
