from flask import Flask, request, g, render_template, redirect, flash, send_file,url_for, send_from_directory
import os
import api.users_login as amp
from api.users_registation import *
from db.db_config import *

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = get_db()


@app.route('/api/login', methods=['POST'])
def login():
    return amp.login()


@app.route('/api/register', methods=['POST'])
def register():
    return register_user()


@app.after_request
def after_request(response):
    g.db.commit()
    return response
