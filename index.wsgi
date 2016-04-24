import sae
from musicall.musicall import wsgi

application = sae.create_wsgi_app(wsgi.application)
