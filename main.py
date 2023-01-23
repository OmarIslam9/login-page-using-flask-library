from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def hi():
    return render_template("index.html")

@app.route("/welcome",methods=["post"])
def recive_data():
    name=request.form["firstname"]
    sec=request.form["lastname"]
    bd=request.form["dob"]
    email=request.form["email"]
    address=request.form["address"]
    return f"{name},{sec},{bd},{email},{address}"








if __name__=="__main__":
    app.run(debug=True)
