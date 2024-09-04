import psycopg2
import os

from dotenv import load_dotenv


def get_connection():
    load_dotenv()
    return psycopg2.connect(
        host = os.getenv('PGHOST'),
        user = os.getenv('PGUSER'),
        password = os.getenv('PGPASSWORD'),
        databgase = os.getenv('PGDATABASE'),
        port = os.getenv('PGPORT'),
    )
