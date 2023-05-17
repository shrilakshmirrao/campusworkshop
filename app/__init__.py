"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi92eu4dadc9vmh1i7g-a.oregon-postgres.render.com",
        database="todo_lr7x",
        user="root",
        password="G8DSaW1mDWuK7JewNzOSemhw56s3kCv5")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
