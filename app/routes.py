from flask import Blueprint, request, jsonify
from .models import Post, db

# Create a Blueprint for the blog routes
blog = Blueprint('blog', __name__)

# Create a new post
@blog.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created!"}), 201

# Get all posts
@blog.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    result = [{"id": post.id, "title": post.title, "content": post.content, "date_posted": post.date_posted} for post in posts]
    return jsonify(result), 200

# Get a post by ID
@blog.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({"id": post.id, "title": post.title, "content": post.content, "date_posted": post.date_posted}), 200

# Update a post
@blog.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
