from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print("Received POST:")
        print(post_data)
        self.send_response(200)  
        self.end_headers()
        self.wfile.write(b'POST received')  
port = 9765
server_address = ('', port)
print(f"Server HTTP {port}")
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()
