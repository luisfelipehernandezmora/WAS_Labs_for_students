from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import timezone
from sqlalchemy import DateTime
from sqlalchemy import text
import uuid
import re
import os
import requests

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
"""

Create required tables in SQLite Database

"""
class User(db.Model):
    userid = db.Column(db.String(200), nullable=False, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, password, userid=None):
        if userid == None:
            self.userid = str(uuid.uuid4()) 
        else:
            self.userid = userid
        self.username = username
        self.password = password

class Note(db.Model):
    noteid = db.Column(db.String(200), nullable=False, primary_key=True)
    userid = db.Column(db.String(200), nullable=False)
    notetitle = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(400), nullable=False)

    def __init__(self, userid, notetitle, note):
        self.userid = userid
        self.noteid = str(uuid.uuid4()) 
        self.note = note
        self.notetitle = notetitle

#db.drop_all()
db.create_all()
"""

Begin routing

"""

@app.route('/', methods=['GET'])
def index(): 
    return render_template("index.html")

@app.route("/", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username != None and password != None:
        # Get all users with username
        user = User.query.filter_by(username=username).first()

        """
        If no user with that username, register the user
        If there is a user with that username, 
        See if password matches
        """
        if user is None:
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return render_template("index.html", message="Registration success")
        else:
            if user.password != password:
                return render_template("index.html", message="Incorrect username or password!")
            else:
                response = redirect("/dashboard")
                response.set_cookie('userid', user.userid)
                return response

@app.route("/dashboard", methods=["GET"])
def dashboard():
    """
    only list notes of users if has a valid userid cookie
    using userid is safe since it is secretly stored in database
    """ 
    userid = request.cookies.get('userid')
    if userid:
        user = User.query.filter_by(userid=userid).first()
        if user is not None:
            notes = Note.query.filter_by(userid=userid).all()
            return render_template("dashboard.html", username=user.username, notes=notes)
        else:
            return redirect("/")    
    return redirect("/")    

@app.route("/report/<note_id>", methods=["GET"])
def report(note_id):
    r = requests.get("http://0.0.0.0:8080/?url=http://0.0.0.0:8888/note/"+note_id)
    return r.text


@app.route("/dashboard", methods=["POST"])
def create_post():
    """
    Notes are created only if a valid userid is in cookie
    """
    userid = request.cookies.get('userid')
    note = request.form.get("note")
    notetitle = request.form.get("notetitle")
    if userid:
        user = User.query.filter_by(userid=userid).first()
        if user is not None:
            note = Note(userid, notetitle, note)
            db.session.add(note)
            db.session.commit()
            return redirect("/dashboard")
        else:
            return redirect("/")    
    return redirect("/")    


@app.route("/note/<note_id>", methods=["GET"])
def preview_note(note_id):
    note = Note.query.filter_by(noteid=note_id).first()
    if note is None:
        return redirect("/")
    else:
        script_tag = re.compile(re.escape('script'), re.IGNORECASE)
        note_txt = note.note.replace("\"","'")
        note_txt = note_txt.replace("onerror", "")
        note_txt = re.sub(script_tag, "X", note_txt)
        return render_template("preview_note.html", title=note.notetitle, note=note_txt)

@app.route("/logout", methods=['GET'])
def logout():
    response = redirect("/")
    response.set_cookie('userid', '', expires=0)
    return response

@app.route("/source")
def source():
    return open("app.py").read()



if __name__ == "__main__":
    print("LIstetning on 8888",flush=True)
    app.run(host='0.0.0.0', port=8888, debug=True)

