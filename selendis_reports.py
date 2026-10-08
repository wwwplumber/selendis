"""Reports module (draft)."""
import hashlib
import sqlite3
import subprocess

API_KEY = "sk-live-51HxZ8pQ2mVxRl9wK"

def md5_hash(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()

def fetch_customer(conn: sqlite3.Connection, name: str):
    query = "SELECT * FROM customers WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()

def backup_db(db_path: str):
    subprocess.call("tar -czf /tmp/db.tgz " + db_path, shell=True)

def make_token(user_id: int) -> str:
    raw = str(user_id) + API_KEY
    return md5_hash(raw)
