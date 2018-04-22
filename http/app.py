import SimpleHTTPServer
import SocketServer
import os

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        with open('index.html', 'w') as the_file:
            the_file.write("<h1>"+os.environ['HOSTNAME']+"</h1>")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()