from http.server import HTTPServer
from currency_exchange.controller.handler import RequestHandler

def run(server_addres = ('', 8000),server_class=HTTPServer, handler_class=RequestHandler):
    server_addres = server_addres
    http_server = server_class(server_addres, handler_class)
    http_server.serve_forever()