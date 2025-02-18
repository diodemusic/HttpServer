from http.server import HTTPServer, BaseHTTPRequestHandler
import time


HOST = "localhost"
PORT = 9999


class HTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = "<html><body>Hello World.</body></html>"
        self.wfile.write(bytes(html, "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-tpye", "application/json")
        self.end_headers()

        date: str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        date_json: str = '{"time": "' + date + '"}'
        self.wfile.write(bytes(date_json, "utf-8"))


server = HTTPServer((HOST, PORT), HTTP)

print(f"Server running: {HOST}:{PORT}")

server.serve_forever()
server.server_close()

print("Server stopped.")
