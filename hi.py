from flask import Flask, redirect, url_for  #import statements

app = Flask(__name__)

@app.route("/")   #default application decorator
def hello():
    return "Hello,  Welcome to CAD "
#app.add_url_rule("/", 'hello', hello)

@app.route('/hello/<name>')  #< > the betweeen one will become variable
def name(name):
    return "Hello %s" % name    #CREATING A DYNAMIC ROUTES BY USING THE VARIABLE IN DECORATOR

# <STRING>,<int : number> , <float: fvalue>
@app.route("/hello/<int:batchnumber>")
def batch(batchnumber):
    return " Hello CAD Batch {} Students " .format(batchnumber)


@app.route("/student/<day>")
def day_student(day):
    if day == "monday":
        batchnumber = 1
        return redirect(url_for('batch', batchnumber = batchnumber))
    elif day == 'friday':
        batchnumber = 5
        return redirect(url_for('batch', batchnumber = batchnumber))
    else :
        return "You are not in the Batch that guide by MAHIDHAR"



if __name__ == "__main__":
    app.run(debug=True)


#local host : http://127.0.0.1:   
#port : 5000
#debug = False