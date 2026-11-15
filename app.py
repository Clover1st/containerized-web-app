from http.server import HTTPServer, BaseHTTPRequestHandler
import redis
import psycopg2
import json

r = redis.Redis(host='redis', port=6379)

def get_db():
    return psycopg2.connect(
        host="postgres",
        database="appdb",
        user="clover",
        password="password123"
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        count = r.incr('visits')
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT username, created_at FROM users')
        users = cur.fetchall()
        cur.close()
        conn.close()
        
        self.send_response(200)
        self.end_headers()
        response = f"Clover was here. Total visits: {count}\n\nRegistered Users:\n"
        for user in users:
            response += f"- {user[0]} (joined: {user[1]})\n"
        self.wfile.write(response.encode())

init_db()
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
