from http.server import HTTPServer, BaseHTTPRequestHandler


class SavesServer(BaseHTTPRequestHandler):
    def get_html(self):
        with open("content/index.html", "r") as f:
            return f.read()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        html = self.get_html()
        self.wfile.write(bytes(html, "utf-8"))


class Server(BaseHTTPRequestHandler):
    server = None
    html = ""

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def run(self):
        self.server = HTTPServer((self.address, self.port), SavesServer)
        print(f"Server running on {self.address}:{self.port}")
        self.server.serve_forever()

    def stop(self):
        self.server.server_close()


server = Server("localhost", 9999)
server.run()
server.stop()
