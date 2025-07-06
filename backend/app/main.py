from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def connect():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", 5432),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
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
