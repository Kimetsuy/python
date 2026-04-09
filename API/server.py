from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('teste', '123')
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title>Teste</title>
                </head>
                <body>
                    <h1>Teste</h1>
                    <p>Teste</p>
                </body>
            </html>
            """
            self.wfile.write(data.encode())
        elif self.path == '/teste':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title>Lorem</title>
                </head>
                <body>
                    <h1>lorem ipsum</h1>
                    <p>Lorem ipsum dolor sit amet</p>
                </body> 
            """
            self.wfile.write(data.encode())
server = HTTPServer(('localhost', 8000), Handler)
server.serve_forever()