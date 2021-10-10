from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

#Render página de inicio.
@app.route("/")
def index():
    users = User.get_all()
    return render_template("read_all.html", all_users = users)

#Link para el formulario para agregar un contacto.
@app.route("/newUser")
def displayForm():
    return render_template("create.html")

#Show Data
@app.route('/show', methods=['POST'])                           
def displayShow():
    id = request.form['id']
    result = User.find_Data(id)
    return render_template("show.html", edit_data = result)

#Paso 1 edición: Link para llegar al formulario de edición:
@app.route('/edit', methods=['POST'])                           
def displayEdit():
    id = request.form['id']
    result = User.find_Data(id)
    return render_template("edit.html", edit_data = result)

#Paso 2 edición: Cambiar:
@app.route('/update', methods=['POST'])                           
def userEdit():
    id = request.form['id'],
    fname= request.form["fname"],
    lname = request.form["lname"],
    email = request.form["email"]
    result = User.update_Data(id, fname, lname, email)
    return redirect ("/")

   



#Generar un  contacto nuevo
@app.route("/AddUser", methods=["POST"])
def addUser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    result= User.add_user(data)
    return redirect('/')

#test
#@app.route("/test", methods=["POST"])
#def test():
#    data = {
#        "id": request.form["id"],
#        "newfname": request.form["newfname"],
#        "newlname" : request.form["newlname"],
#        "newemail" : request.form["newemail"]        
#    }
#    result=User.update_user(data)
#    return redirect('/')

#Borrar el contacto
@app.route('/delete', methods=['POST'])                           
def deleteValues():
    id = request.form['id']
    delete = User.delete_user(id)
    return redirect('/')

#Editar el contacto
#@app.route('/EditUser', methods=["POST"])
#def editUser():
#    data = {
#        "id": request.form['id'],
#        "fname": request.form["fname"],
#        "lname" : request.form["lname"],
#        "email" : request.form["email"]
#    }
#    User.edit_user(data)
#    return redirect('/show')

#@app.route('/show', methods=["GET"])
#def editUser():
#    User.show_user()
#    return render_template('show.html')





if __name__ == "__main__":
    app.run(debug=True)