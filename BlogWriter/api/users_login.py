import sqlite3 as sq
from flask import Flask, request, g
from utils.uitils import *
import json


def login():
    if request.method == 'POST':
        data = request.json
        # Check if account exists using sqlite
        cursor = g.db.execute("SELECT * FROM user WHERE Username=? AND password=?",
                              (data['username'], data['password']))
        data = cursor.fetchall()
        user_data = [{'ID': row[0], 'NAME': row[1], 'PASSWORD': row[2],'EmailId': row[3],
                      'Phone': row[4], 'DOB': row[5], 'Gender': row[6]} for row in data]

        # If account exists in user table in  database
        if len(data) == 1:
            return onsuccess_response(user_data, 'You have logged in successfully')
        else:
            return onsuccess_message('No user found')

    return onerror_response('This is POST method')



