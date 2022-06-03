import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from generate.maker import generate as generator
from tempfile import mkdtemp
from model.find_wally import find_wally
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

@app.route("/auto", methods =  ['GET','POST'])
def auto():
    if request.method == "POST":
        
        image1  = find_wally("static/auto_images/1.jpg", '1')
        image2  = find_wally("static/auto_images/2.jpg", '2')
        image3  = find_wally("static/auto_images/3.jpg", '3')
        image4  = find_wally("static/auto_images/4.jpg", '4')
        return render_template("auto.html", image1 = image1, image2 = image2, image3 = image3, image4 = image4)
    else:
        return render_template("auto.html")



@app.route("/generate", methods=['GET', 'POST'])
def generate():
    if request.method == "POST":  
        temp = generator()
        return render_template("generate.html",value1=(temp[0] * 0.2)+10,value2=800 - (temp[1] * 0.2))
    else:
        return render_template("generate.html")
    
    

@app.route("/man")
def man():
    if request.method == "POST":
        return render_template("man.html")
    else:
        return render_template("man.html")
    