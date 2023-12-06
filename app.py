from flask import *
import pymysql
# create the app 
app=Flask(__name__)
connection=pymysql.connect(host="localhost",user="root",database="coffee",password="")
@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method=='POST':
        #TODO
        #The body of if
        # get the data from the form 
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm_password']

# input validation
        if password != confirm:
            return render_template("signup.html",message= "passwords do not match")

        # save the user in to users list 
        user={
            "username":username,
            "email":email,
            "password":password
        }
       
        return render_template("signup.html",message="user saved sucessfully")

  
    else:
        return render_template("signup.html")












app.run(debug=True,port=8800)

