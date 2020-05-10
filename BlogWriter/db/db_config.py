import sqlite3 as sq
import os
from flask import current_app, g

DATABASE_DIR = os.getcwd()
DB_NAME = 'USER.db'
TABLE_NAME = 'user'
DATABASE_PATH = DATABASE_DIR + '\\' + DB_NAME
print(DATABASE_PATH)


def get_db():
    """
    this method returns the data base object
    :return: db object
    """
    if 'db' not in g:
        g.db = sq.connect(DATABASE_PATH, detect_types=sq.PARSE_DECLTYPES)
        g.db.row_factory = sq.Row


    return g.db


