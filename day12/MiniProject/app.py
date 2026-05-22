from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form["name"]
    email=request.form["email"]
    message=request.form["message"]
    return render_template("success.html", username=name,useremail=email,usermessage=message)

if __name__=="__main__":
    app.run(debug=True)