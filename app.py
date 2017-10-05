# Team Turbo Funiculator
# Samantha Ngo, Helen Ye, Shaina Peters
# SoftDev -- pd7
# hw07 -- Do I know you?
# 2017-10-04

# Import all necessities
from flask import Flask, render_template, request, session
import os

# Create instance of class
app = Flask(__name__) 

# Hard-coded username and password
username = "jeff_sessions123"
password = "Super secret password"

# Generate secret key to make cookies immutable to others.
app.secret_key = os.urandom(32)

# If initially loading the webpage, load the login page.
# If they're already logged in, then load the welcome page.
@app.route("/")
@app.route("/login")
def login():
    print "Session.get('Jeff') returns ", session.get("Jeff")
    if session.get("Jeff") == username:
        return render_template('welcome.html',
                               username = username)
    else:
        return render_template('login.html',
                               msg = "")

# Authentification Process
@app.route("/auth", methods=["POST"])
def authentification():
    # Get user-inputted username and password from the form
    userIn = request.form["username"]
    print "U: " + userIn
    passIn = request.form["password"]
    print "P: " + passIn

    # If username and password are correct... 
    if userIn == username and passIn == password:
        # ...open a new session and...
        session["Jeff"] = userIn
        # ...render the welcome page.
        return render_template("welcome.html",
                               username = userIn)
    # Otherwise, render the login page(again) with an error message.
    else:
        return render_template("login.html",
                               msg = "Incorrect username or password. Nice try, Jeff Sessions. ")

# Logging out renders the login page.
# Should it reroute to the login page instead?
@app.route("/logout")
def logout():
    # End the session
    session["Jeff"] = ""
    # Render Login Page
    return render_template("login.html",
                            msg = "Logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
