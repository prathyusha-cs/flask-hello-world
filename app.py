from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Fetch database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logging.error("DATABASE_URL is not set! Flask cannot connect to the database.")

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Define User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


# Define Post table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return f"<Post {self.title}>"


# Route to create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201


# Route to get all users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])


# Route to create a new post
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    new_post = Post(title=data["title"], content=data["content"], user_id=data["user_id"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created!"}), 201


# Route to get all posts
@app.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([
        {"id": p.id, "title": p.title, "content": p.content, "user_id": p.user_id}
        for p in posts
    ])


@app.route("/", methods=["GET"])
def get_main_page():
    return jsonify("hello")

@app.route("/check", methods=["GET"])
def get_main_page():
    return jsonify("github actions working")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
