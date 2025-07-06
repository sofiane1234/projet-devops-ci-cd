from fastapi import FastAPI
import psycopg2
import os
import json

app = FastAPI()

def extract(val, default=None):
    try:
        return json.loads(val)["value"]
    except Exception:
        return val or default

def connect():
    return psycopg2.connect(
        host=extract(os.getenv("DB_HOST"), "localhost"),
        port=int(extract(os.getenv("DB_PORT"), 5432)),
        database=extract(os.getenv("DB_NAME"), "employees"),
        user=extract(os.getenv("DB_USER"), "postgres"),
        password=extract(os.getenv("DB_PASSWORD"), "postgres"),
        sslmode="require",              # SSL obligatoire pour Azure PostgreSQL
        connect_timeout=5
    )

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API employé"}

@app.get("/health-db")
def health_db():
    try:
        conn = connect()
        conn.close()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/employees")
def get_employees():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, role FROM employees;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]
    except Exception as e:
        return {"error": str(e)}
