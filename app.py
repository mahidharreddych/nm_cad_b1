from flask import Flask, redirect, url_for, render_template,request, flash

app = Flask(__name__)
app.secret_key = 'something'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/course")
def course():
    return render_template("courses.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/contact", methods = ['POST', 'GET'])
def contact():
    if request.method == 'POST':
        u_name = request.form['fullname']
        u_email = request.form['email']
        u_pnumber = request.form['pnumber']
        u_course = request.form['course']
        enquiry_list = [u_name, u_email, u_course, u_pnumber]
        print(enquiry_list)
        print("hello")
        flash(" Your details have been succesfully submitted", 'error')
        return render_template("courses.html")
    return render_template("contact.html")


@app.route("/contact_file", methods = ['POST', 'GET'])
def file():
    f = request.files['details_file']
    f.filename
    f.save(f.filename + ".docx")
    return "file uplaod successfull"



if __name__ == "__main__":
    app.run(debug=True)