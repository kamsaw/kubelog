from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print("Otrzymano POST:")
        print(post_data)
        self.send_response(200)  
        self.end_headers()
        self.wfile.write(b'POST received')  
port = 8080
server_address = ('', port)
print(f"Server HTTP {port}")
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()
