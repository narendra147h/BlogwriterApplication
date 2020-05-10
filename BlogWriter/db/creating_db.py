import sqlite3 as sq
from db.db_config import *
import os

conn = sq.connect(DATABASE_PATH)
cur = conn.cursor()

conn.execute('CREATE TABLE if not exists ' + TABLE_NAME + ' (' +
             'ID TEXT PRIMARY KEY NOT NULL, '
             'username TEXT NOT NULL, '
             'password TEXT NOT NULL, ' 
             'emailid TEXT NOT NULL, '
             'phone TEXT NOT NULL,'
             'DOB TEXT NOT NULL,'
             'gender TEXT NOT NULL' + ' );')

conn.commit()
conn.close()





