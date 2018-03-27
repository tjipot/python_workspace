# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
    '/wx', 'Handle',
)

class Handle(object):
    def GET(self):
        return "hello, this is a test"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

'''
Log:
====
http://127.0.0.1:8080/wx
http://localhost:8080/wx
http://0.0.0.0:8080/wx
====
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/UNIVESRE/Documents/workspace_python/com/univesre/demo/wxmp/main.py
http://0.0.0.0:8080/
127.0.0.1:58816 - - [27/Mar/2018 18:14:02] "HTTP/1.1 GET /wx" - 200 OK
127.0.0.1:58816 - - [27/Mar/2018 18:14:03] "HTTP/1.1 GET /favicon.ico" - 404 Not Found
127.0.0.1:58826 - - [27/Mar/2018 18:14:17] "HTTP/1.1 GET /wx" - 200 OK
127.0.0.1:58835 - - [27/Mar/2018 18:14:24] "HTTP/1.1 GET /wx" - 200 OK
127.0.0.1:58835 - - [27/Mar/2018 18:14:25] "HTTP/1.1 GET /favicon.ico" - 404 Not Found
'''
