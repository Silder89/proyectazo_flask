from sqlalchemy import inspect
from app import app, db

with app.app_context():
    print("Tablas en la base de datos:", inspect(db.engine).get_table_names())
