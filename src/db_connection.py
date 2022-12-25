import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect("highscores.db")
connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection
