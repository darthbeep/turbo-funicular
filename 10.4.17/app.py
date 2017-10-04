from flask import Flask, render_template, request, session
app = Flask(__name__) # create instance of class

# Naming the session
session["Jeff"] = ""
session["username"] = ""
session["password"] = ""

# Initially loading the webpage
@app.route("/", methods=["POST"])
def login():
    if session["username"] != "":
        return render_template('welcome.html')
    elif session["username"] == "":
        print "200: Login page loaded"
        return render_template('login.html')

@app.route("/auth")
def authentification():
    # Get user-inputted username and password
    username = request.args["username"]
    password = request.args["password"]

    if username == "
    render_template('runMe.html',name=form["username"].value)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
