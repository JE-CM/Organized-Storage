# server.py

# Provide a central server executable which connects to all other project components

from http.server import SimpleHTTPRequestHandler, HTTPServer


class WebHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve an HTML file
        if self.path == "/":
            self.path = "index.html"
        if self.path == "/login":
            self.path = "login.html"
        return SimpleHTTPRequestHandler.do_GET(self)


class Server:
    def __init__(self, server_id, port=8080):
        self.server_id = server_id
        self.web_server, self.web_server_port = self.create_server(port=port)

    def create_server(
        self, server_class=HTTPServer, handler_class=WebHandler, port=8080
    ):
        server_address = ("", port)
        httpd = server_class(server_address, handler_class)
        return httpd, port


def start_db():
    print("TODO")


def analyze_client_data():
    print("TODO")


def main():
    server = Server("organized_storage")
    print(f"Server running on port {server.web_server_port}...")
    server.web_server.serve_forever()


main()
