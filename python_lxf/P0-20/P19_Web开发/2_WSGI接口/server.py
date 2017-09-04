# server.py
# Import From Module wsgiref:
from wsgiref.simple_server import make_server
# Import The applecation() We Wrote:
from hello import application

# Create A Server, The IP Address Is Empty, Port Is 8000, Handling Function Is application():
httpd = make_server('', 8000, application)
print('Serving HTTP on Port 8000...')
# Begin HTTP Request Listening...
httpd.serve_forever()


