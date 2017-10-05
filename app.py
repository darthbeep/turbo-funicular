'''
Samantha Ngo, Shaina Peters, Helen Ye
SoftDev1 pd7
HW07 -- Do I know you?
2017-10-04
'''

# Import all necessities
from flask import Flask, render_template, request, session
import os
app = Flask(__name__) # create instance of class

# Declare our username/password combo
username = "jeff_sessions123"
password = "Super secret password"

# Define a secret key
app.secret_key = os.urandom(32)

# Initially loading the webpage, load the welcome page
# if they're logged in
@app.route("/")
@app.route("/login")
def login():
    if session.get("jeff") == username:
        return render_template('welcome.html',
                               username = username)
    else:
        return render_template('login.html',
                               msg = "")

@app.route("/auth", methods=["POST"])
def authentification():
    # Get user-inputted username and password
    userIn = request.form["username"]
    passIn = request.form["password"]
    # Authenticate user
    if userIn == username and passIn == password:
        session["jeff"] = userIn
        return render_template("welcome.html",
                               username = username)
    elif userIn != username:
        return render_template("error.html",
                               msg = "Incorrect user")
    else:
        return render_template("error.html",
                               msg = "Incorrect pass")

# Log out the user by resetting the session
@app.route("/logout")
def logout():
    session["jeff"] = ""
    return render_template("login.html",
                            msg = "Logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
