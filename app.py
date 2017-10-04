from flask import Flask, render_template, request, session
import os
app = Flask(__name__) # create instance of class

username = "jeff_sessions123"
password = "Super secret password"

app.secret_key = os.urandom(32)

# Initially loading the webpage, load the welcome page
# if they're logged in
@app.route("/")
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
    if userIn == username and passIn == password:
        session["jeff"] = userIn
        return render_template("welcome.html",
                               username = username)
    else:
        return render_template("login.html",
                               msg = "Incorrect user or pass")

@app.route("/logout")
def logout():
    session["jeff"] = ""
    return render_template("login.html",
                            msg = "Logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
