from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres")
    )
    return conn

@app.route("/")
def home():
    return "Flask + PostgreSQL DevOps Project"

@app.route("/db")
def db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"PostgreSQL version: {db_version}"
    except Exception as e:
        return f"Database error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
