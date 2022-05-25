import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from generate.maker import generate as generator
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import json
import re

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/auto")
def auto():
    return render_template("auto.html")

@app.route("/generate", methods=['GET', 'POST'])
def generate():
    generator()
    return render_template("generate.html")

@app.route("/man")
def man():
    return render_template("man.html")