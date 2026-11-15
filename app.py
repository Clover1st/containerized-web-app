from flask import Flask, request, jsonify
import redis
import psycopg2
import hashlib

app = Flask(__name__)
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
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def home():
    count = r.incr('visits')
    return jsonify({
        "message": "Welcome to Clover's app",
        "total_visits": count
    })

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', 
                   (username, password))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": f"User {username} registered successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT id FROM users WHERE username=%s AND password=%s', 
                   (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            return jsonify({"message": f"Welcome back {username}!"})
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users', methods=['GET'])
def users():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT username, created_at FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"username": u[0], "joined": str(u[1])} for u in users])

with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
