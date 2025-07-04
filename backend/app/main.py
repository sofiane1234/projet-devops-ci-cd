from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


def connect():
    return psycopg2.connect(
        host="pg-sosso-devops-ci-cd.postgres.database.azure.com",
        database="employeesdb",
        user="adminuser@pg-sosso-devops-ci-cd",
        password="SuperSecretPassword123"
    )


@app.get("/employees")
def get_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM employees;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "role": r[2]} for r in rows]


@app.get("/")
def root():
    return {"message": "Bienvenue dans l’API employé"}
