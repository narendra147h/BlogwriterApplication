import sqlite3 as sq
import db.db_config as bsd

conn = sq.connect(bsd.DATABASE_PATH)
print('Opend database successfully')

id = input('Enter user id: \n')
username = input('Enter user name: \n')
password = input('Enter the password : \n')
emailid = input('Enter user emailid: \n')
dob = input('Enter user dob: \n')
phone = input('Enter user Phone number: \n')
gender = input('Enter user Gender: \n')

query = ('INSERT INTO user (id, username, password,  emailid, phone, dob, gender)'
         ' VALUES (:ID, :NAME,:PASSWORD, :EmailId, :Phone,  :DOB, :Gender);')

param = {
    'ID': id,
    'NAME': username,
    'PASSWORD': password,
    'EmailId': emailid,
    'Phone': phone,
    'DOB': dob,
    'Gender': gender
        }


conn.execute(query, param)

conn.commit()
conn.close()

