from flask import Flask, render_template, redirect,request


app=Flask(__name__)


# @app.route("/test")
# @app.route("/")
# def hompage():
#     return render_template("home.html",name="Sakthi", age="23")


# @app.route("/login")
# def loginpage():
#     print("inside login")
#     return redirect("/")


@app.route("/",methods=["GET","POST"])
def hompage():
    if request.method=="POST":
        my_name=request.form["my_box"]
        my_age=request.form["my_age"]
        return render_template("home.html",name=my_name,age=my_age)
    print("get method")
    return render_template("index.html")


    
if __name__=="__main__":
    app.run(debug=True,port=5001)


