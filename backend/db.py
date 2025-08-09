import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

# Lee variables desde backend/.env en desarrollo
load_dotenv()

def get_conn():
    return psycopg.connect(
        host=os.getenv("PG_HOST"),
        port=os.getenv("PG_PORT"),
        dbname=os.getenv("PG_DB"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD"),
        row_factory=dict_row,
    )

def query_all(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params or [])
            return cur.fetchall()

def query_one(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params or [])
            return cur.fetchone()

def execute(sql, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params or [])
            conn.commit()
