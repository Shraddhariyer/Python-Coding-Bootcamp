#Expense Tracker
from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    connection=sqlite3.connect("expenses.db")
    cursor=connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expense(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT NOT NULL, amount REAL NOT NULL, date TEXT NOT NULL) """)
    if request.method=="POST":
        category=request.form["category"]
        amount=request.form["amount"]
        date=request.form["date"]
        cursor.execute("""INSERT INTO expense(category,amount,date)VALUES(?,?,?)""",(category,amount,date))
        connection.commit()
    cursor.execute("SELECT * FROM expense")
    rows=cursor.fetchall()
    connection.close()
    return render_template("index.html",expense=rows)


if __name__=="__main__":
    app.run(debug=True)