from flask import Flask, render_template, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app=Flask(__name__)
app.secret_key="secret"

connection=sqlite3.connect("users.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)""")
connection.commit()
connection.close()
@app.route("/")
def home():
    return redirect("/register")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        hashed=generate_password_hash(password)
        connection=sqlite3.connect("users.db")
        cursor=connection.cursor()
        cursor.execute("INSERT INTO users VALUES(?,?)",(username,hashed))
        connection.commit()
        connection.close()
        return redirect("/login")
    return render_template("register.html")
    
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        connection=sqlite3.connect("users.db")
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?",(username,))
        user=cursor.fetchone()
        connection.close()
        if user:
            saved_password=user[1]
            if check_password_hash(saved_password,password):
                session["user"]=username
                return redirect("/dashboard")
        return "Wrong username or Password"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html",username=session["user"])

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/login")


if __name__=="__main__":
    app.run(debug=True)
