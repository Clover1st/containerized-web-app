from http.server import HTTPServer, BaseHTTPRequestHandler
import redis

r = redis.Redis(host='redis', port=6379)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        count = r.incr('visits')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Clover was here. Total visits: {count}".encode())

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
