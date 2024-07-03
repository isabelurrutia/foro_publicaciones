from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app

#Importamos los modelos
from flask_app.models.comment import Comment


@app.route("/create_comment", methods=["POST"])
def create_comment():
    if not Comment.validate_comment(request.form):
        return redirect("dashboard")
    Comment.save(request.form)
    return redirect("/dashboard")
