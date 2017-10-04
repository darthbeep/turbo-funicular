from flask import render_template
import cgitb

form = cgi.FieldStorage()
render_template('runMe.html',name=form["username"].value)
render_template('runMe.html',name=form["username"].value)
