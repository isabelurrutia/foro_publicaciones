#terminal: pipenv install flask pymysql flask-bcrypt
#Importar la app
from flask_app import app
#Importar controladores (puede ser mas de uno)
from flask_app.controllers import users_controller, posts_controller, comments_controller
#Ejecucion de app
if __name__=="__main__":
    app.run(debug=True)
    

