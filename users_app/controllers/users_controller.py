from flask import render_template, request, redirect
from users_app import app
from users_app.models.user import User 



#Index page
@app.route("/")
def index():
    users = User.get_all()
    return render_template("read_all.html", all_users = users)

#New post (1/2) - Display form
@app.route("/newUser")
def displayForm():
    return render_template("create.html")

#New post (2/2) - Generate post
@app.route("/AddUser", methods=["POST"])
def addUser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    result= User.add_user(data)
    return redirect('/')

#Show:
@app.route('/show', methods=['POST'])                           
def displayShow():
    id = request.form['id']
    result = User.find_Data(id)
    return render_template("show.html", edit_data = result)

#Edit post (1/2) - Display post
@app.route('/edit', methods=['POST'])                           
def displayEdit():
    id = request.form['id']
    result = User.find_Data(id)
    return render_template("edit.html", edit_data = result)

#Edit post (2/2) -  Change data
@app.route('/update', methods=['POST'])                           
def userEdit():
    id = request.form['id'],
    fname= request.form["fname"],
    lname = request.form["lname"],
    email = request.form["email"]
    result = User.update_Data(id, fname, lname, email)
    return redirect ("/")

#Delete post
@app.route('/delete', methods=['POST'])                           
def deleteValues():
    id = request.form['id']
    delete = User.delete_user(id)
    return redirect('/')