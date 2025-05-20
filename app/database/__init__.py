from flask import g
from app import DATABASE_URL
import sqlite3

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URL)
        db.row_factory = sqlite3.Row  # opcional para acceder a columnas por nombre
    return db
