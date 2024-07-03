from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos los modelos
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment


@app.route("/create_post", methods=["POST"])
def create_post():
    #request.form = {"content": "contenido publicacion", "user_id":1}
    if not Post.validate_post(request.form):
        return redirect("dashboard")
    Post.save(request.form)
    return redirect("/dashboard")

@app.route("/delete_post/<int:id>")
def delete_post(id):
    #metodo que borrar un registro en base a su ID
    dicc = {"id":id}
    Post.delete(dicc)
    return redirect("/dashboard")



