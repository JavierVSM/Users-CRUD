from mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#Editar contacto: Paso 1, llamar lo que debo editar, esto es lo mismo para show, este paso es compartido.
    @classmethod
    def find_Data(cls, id):
        query = "SELECT * FROM users WHERE user_id=%(id)s;"
        data={
            "id":id
        }
        results = connectToMySQL('users_db').query_db(query, data)
        findData = []
        for data in results:
            findData.append(cls(data))
        return findData
        
#Paso 2, actualizar con nuevos datos:
    @classmethod
    def update_Data(cls, id, fname, lname, email):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at= NOW() WHERE user_id=%(id)s;"
        data={
            "id":id,
            "fname": fname,
            "lname": lname,
            "email": email
        }
        return connectToMySQL('users_db').query_db(query, data)

#Render página de inicio.   
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_db').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

#Generar un  contacto nuevo    
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() );"
        return connectToMySQL('users_db').query_db( query, data )

#Borrar el contacto    
    @classmethod
    def delete_user(cls, id):
        query = "DELETE FROM users WHERE user_id=%(id)s;"
        data={
            "id": id
            }
        return connectToMySQL('users_db').query_db( query, data )