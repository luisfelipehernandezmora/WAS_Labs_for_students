from flask import Flask,render_template,request,redirect,session,escape
import sqlite3
import uuid
import os
import socket
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'h4ck3r43v3r9875SDF'
app.config['UPLOAD_FOLDER']="user_posts"
curr_dir = os.path.dirname(os.path.abspath(__file__))
BOT_URL = os.getenv("BOT_URL") or 'http://localhost:3000'


@app.route("/",methods=["GET"])
def main():
    if(session.get("user") != None):
        return redirect("/home/"+session.get("user"),code=302)
    else:
        return redirect("/login")

@app.route("/home/<user>",methods=["GET","POST"])
def home(user):
    if(session.get("loggedin") != "true"):
        return redirect("/login",code=302)
    access=True
    if(user != session.get("user")):
        access=False
    conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
    cursor = conn.cursor()
    query = "select id from posts where username=?"
    result = cursor.execute(query,(user,))
    result = result.fetchall()
    return render_template("home.html",username=session.get("user"),post_list=result,access=access,user=user)

@app.route("/login",methods=["GET","POST"])
def login():
    if(session.get("loggedin") == "true"):
        return redirect("/home/"+session.get("user"),code=302)
    if(request.method=="POST"):
        try:
            user = request.form.get("username").strip()
            passw = request.form.get("password").strip()
            conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
            cursor = conn.cursor()
            query = "select username,password from accounts where username=? and password=?"
            result = cursor.execute(query,(user,passw))
            result = result.fetchone()
            conn.commit()
            if(result != None):
                session["user"] = user
                session["loggedin"] = "true"
                return redirect("/home/"+user,code=302)
            else:
                return render_template("login.html",log_message="WRONG PASSWORD/USERNAME")
        except:
            return render_template("login.html")
    elif(request.method=="GET"):
        return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if(request.method=="POST"):
        try:
            user = request.form.get("username").strip()
            passw = request.form.get("password").strip()
            conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
            cursor = conn.cursor()
            query = "select username from accounts where username=?"
            result = cursor.execute(query,(user,))
            result = result.fetchone()
            if(result != None):
                return render_template("register.html",reg_message="Username already exists")
            query = "insert into accounts values(?,?)"
            result = cursor.execute(query,(user,passw))
            conn.commit()
            if(result):
                    return render_template("register.html",reg_message="SUCCESSFULLY REGISTERED")
            else:
                return render_template("register.html",reg_message="REGISTRATION FAILED")
        except Exception as e:
            return render_template("register.html",reg_message=e)
    elif(request.method=="GET"):
        return render_template("register.html")

@app.route('/makepost', methods = ['POST'])
def makepost():
    if(session.get("loggedin") != "true"):
        return redirect("/login",code=302)
    if(request.method=="POST"):
        try:
            title = request.form.get("title").strip()
            content = request.form.get("body")
            if(len(content)>350):
                return "Content too long"
            conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
            id = uuid.uuid4().hex
            cursor = conn.cursor()
            query = "insert into posts values(?,?,?,?)"
            result = cursor.execute(query,(id,session.get("user"),title,content))
            query = "insert into access_list values(?,?)"
            result = cursor.execute(query,(id,session.get("user")))
            conn.commit()
            if(result):
                    return redirect("/home/"+session.get("user"))
            else:
                return render_template("home.html",post_message="POST FAILED")

        except:
            return render_template("home.html",username=session.get("user"))
    return render_template("home.html",username=session.get("user"))

@app.route("/posts",methods=["GET","POST"])
def posts():
    if(session.get("loggedin") != "true"):
        return redirect("/login",code=302)
    id = request.args.get("id")
    conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
    cursor = conn.cursor()
    query = "select username from access_list where id=?"
    if all(username[0]!=session.get("user") for username in cursor.execute(query,(id,))):
        return "You don't have access to view this post :( <!--pls get permission from admin sir-->"
    query = "select title,content from posts where id=?"
    result = cursor.execute(query,(id,))
    result = result.fetchone()
    return f"""<html>
    <head>
        <title>{ escape(result[0]) }</title>
        <style>
        body{{
            background-color: #072227;
            color: #ffffff;
            font-family: Monospace;
        }}
        </style>
    </head>
    <body>
    <div style="text-align:center">
       <h1>{ result[0] }</h1>
       <p><pre>{ result[1] }</pre></p>
    </div>
    </body>
</html>"""

@app.route("/giveaccess",methods=["POST"])
def giveaccess():
    if(session.get("loggedin") != "true"):
        return redirect("/login",code=302)
    id = request.form.get("id")
    user = request.form.get("user")
    conn = sqlite3.connect(os.path.join(curr_dir,"csrfdb.db"))
    cursor = conn.cursor()
    query = "select id,username from posts where id=? and username=?"
    result = cursor.execute(query,(id,session.get("user")))
    result = result.fetchone()
    if(result == None):
        return "you dont have access to give access"
    query = "select username from accounts where username=?"
    result = cursor.execute(query,(user,))
    result = result.fetchone()
    if(result == None):
        return "user doesnt exist"
    query = "insert into access_list values(?,?)"
    result = cursor.execute(query,(id,user))
    print("access given")
    conn.commit()
    return redirect("/home/"+session.get("user"),code=302)

@app.route("/report",methods=["GET"])
def report():
    id = request.args.get("id")
    if id:
        try:
            int(id, 16)
        except:
            return render_template("report.html",report_message="Invalid id")
        url = f"http://localhost:5000/posts?id={id}"
        requests.get(BOT_URL+f"?url={url}")
        return render_template("report.html",report_message="Admin will check your report shortly")
    return render_template("report.html")
if(__name__=="__main__"):
    app.run(debug=True,host="0.0.0.0")