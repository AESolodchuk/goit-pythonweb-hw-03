from threading import Thread
from time import sleep
from http import client
from server import SimpleHttpRequestHandler
from http.server import HTTPServer

httpd = HTTPServer(("localhost", 8001), SimpleHttpRequestHandler)
server = Thread(target=httpd.serve_forever)
server.start()
sleep(0.5)


h1 = client.HTTPConnection("localhost", 8001)
h1.request("GET", "/")

res = h1.getresponse()
print(res.status, res.read)


data = res.read()
print(data)


httpd.shutdown()
