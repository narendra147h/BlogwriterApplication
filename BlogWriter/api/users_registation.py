import sqlite3 as sq
from flask import Flask, request, g, render_template, session
from utils.uitils import *
import uuid


# register form
def register_user():
    if request.method == 'POST':
        data = request.json
        user_cursor = g.db.execute("SELECT * FROM user WHERE username=? OR emailid=? OR phone=? ",
                              (data["username"], data["email"], data["phone"]))
        if len(user_cursor.fetchall()) >= 1:
            return onsuccess_message("User has already Registered !!")
        else:
            query = ('INSERT INTO User (ID, username, password, emailid, phone, DOB, gender) '
                     ' VALUES (:ID, :USERNAME, :PASSWORD, :EMAIL, :PHONE, :DOB, :GENDER);')
            param = {
                'ID': str(uuid.uuid4()),
                'USERNAME': data["username"],
                'PASSWORD': data["password"],
                'EMAIL': data["email"],
                'PHONE': data["phone"],
                'DOB': data["dob"],
                'GENDER': data["gender"]
            }
            g.db.execute(query, param)
            g.db.commit()
            data_cursor = g.db.execute("SELECT * FROM user WHERE username=? OR emailid=? OR phone=? ",
                                  (data["username"], data["email"], data["phone"]))
            data = data_cursor.fetchall()
            user_data = [{'ID': row[0], 'NAME': row[1], 'PASSWORD': row[2], 'EmailId': row[3],
                          'Phone': row[4], 'DOB': row[5], 'Gender': row[6]} for row in data]
            return onsuccess_response(user_data, "You have Registered Successfully !!")
