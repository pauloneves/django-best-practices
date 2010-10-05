import os, sys
import site
 
# put virtualenv on pythonpath
site.addsitedir('/opt/webapps/domain.com/lib/python2.6/site-packages')
 
# redirect print statements to apache log
sys.stdout = sys.stderr
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'domain.settings'
 
import django.core.handlers.wsgi
 
application = django.core.handlers.wsgi.WSGIHandler()