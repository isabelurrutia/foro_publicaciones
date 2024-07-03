from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Post:
    def __init__(self, data):
        #data = {diccionario con info de mi base de datos} 
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

        self.user_name = data["user_name"]

    #metodo para guardar, recibe form = {"content": "contenido de la publicacion", "user_id":1}
    @classmethod
    def save(cls, form):
        query = "INSERT INTO posts (content, user_id) VALUES (%(content)s, %(user_id)s)"
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def validate_post(form):
        #form = {"content": "contenido de la publicacion", "user_id":1}
        is_valid =True

        if len(form["content"]) < 1:
            flash("Post content is required.", "post")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT posts.*, users.first_name as user_name FROM posts JOIN users ON posts.user_id = users.id ORDER BY created_at DESC;"
        results = connectToMySQL("foro_publicaciones").query_db(query)
        posts=[]
        for p in results:
            #p = {"id":1, "content":"Hola"..., "user_name":"Elena"}
            posts.append(cls(p))
        return posts
    
    @classmethod
    def delete(cls, data):
        #data = {"id":2}
        query = "DELETE FROM posts WHERE id=%(id)s"
        connectToMySQL("foro_publicaciones").query_db(query, data)
