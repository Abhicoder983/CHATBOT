from vercel_wsgi import handle
from registration.wsgi import application  # Replace 'myproject' with your actual Django project name

app = handle(application)
