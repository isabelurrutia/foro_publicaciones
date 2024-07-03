from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Comment:
    def __init__(self, data):
        #data = {diccionario con info de mi base de datos} 
        self.id = data["id"]
        self.text = data["text"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.post_id = data["post_id"]
        self.user_id = data["user_id"]
        self.user_name_com = data["user_name_com"]

    #metodo para guardar, recibe form = {"text": "contenido del comentario", "post_id":1}
    @classmethod
    def save(cls, form):
        query = "INSERT INTO comments (text, post_id, user_id) VALUES (%(text)s, %(post_id)s, %(user_id)s)"
        print(query)
        return connectToMySQL("foro_publicaciones").query_db(query, form)
    
    @staticmethod
    def validate_comment(form):
        #form = form = {"text": "contenido del comentario", "post_id":1}
        is_valid =True

        if len(form["text"]) < 1:
            flash("Comment content is required.", "comment")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT comments.*, users.first_name as user_name_com FROM comments JOIN posts ON comments.post_id = posts.id JOIN users ON comments.user_id = users.id;"
        results = connectToMySQL("foro_publicaciones").query_db(query)
        print(query)
        comments=[]
        for c in results:
            #c = {"id":1, "text":"Hola"..., "user_name":"Elena"}
            comments.append(cls(c))
        print(comments)
        return comments