from flask import Flask, render_template, request, session
app = Flask(__name__) # create instance of class

# assign following fxn to run when root route requested
@app.route("/")
def login():
    print "200: Login page loaded"
    return render_template('login.html')

#@app.route("/auth")
#def names():
#    render_template('runMe.html',name=form["username"].value)
    
if __name__ == "__main__":
    app.debug = True
    app.run()
