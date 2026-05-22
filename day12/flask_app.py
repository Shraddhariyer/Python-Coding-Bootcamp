from flask import Flask,render_template,request
#create flask app
app=Flask(__name__)


#route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user",methods=["POST"])
def user_profile():
    user_name=request.form["name"]
    return render_template("user.html",username=user_name)


if __name__=="__main__":
    app.run(debug=True)