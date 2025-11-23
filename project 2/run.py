from flask import Flask, request, render_template

app = Flask ( __name__)

@app.route("/",methods=["POST","GET"])
def home_page():
    if request.method == "POST":
        try:
            c_name=request.form["company_name"]
            c_address=request.form["company_address"]
            c_pincode=request.form["pincode"]
            c_mobile_no=request.form["mobile_number"]
            c_email_id=request.form["email_id"]
            c_website=request.form["website"]
            return render_template("htmlindex.html",company_name=c_name,address=c_address,
                                pincode=c_pincode,mobile_number =c_mobile_no,
                                email_id=c_email_id,website=c_website)
        except:
            return render_template("htmlform.html")
    else:
        return render_template("htmlform.html")

if __name__ == "__main__":
    app.run(debug=True)