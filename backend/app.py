from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route("/",methods=["GET"])
def Home():
    return "Welcome to Backend!!"

if __name__ == "__main__":
    from routes.user_routes import user_bp
    app.register_blueprint(user_bp,url_prefix="/user")
    app.run(debug=True,port=8080)
