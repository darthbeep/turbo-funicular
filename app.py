from flask import Flask, render_template, request, session
app = Flask(__name__) # create instance of class

session["jeff"] = ""
password = "Super secret password"

# Initially loading the webpage, load the welcome page
# if they're logged in
@app.route("/", methods=["POST"])
def login():
    if session.get("jeff") == "jeff_sessions123":
        return render_template('welcome.html')
    else:
        return render_template('login.html')

@app.route("/auth")
def authentification():
    # Get user-inputted username and password
    userIn = request.form["username"]
    passIn = request.form["password"]
    if userIn == username and passIn == password:
        session["jeff"] = userIn
        return render_template("welcome.html")
    else:
        return render_template("login.html",
                               error_msg = "Incorrect user or pass")

if __name__ == "__main__":
    app.debug = True
    app.run()
