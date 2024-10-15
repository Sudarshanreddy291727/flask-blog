from flask import Blueprint, request, jsonify, render_template
from .models import Post, db

# Create a Blueprint for the blog routes
blog = Blueprint('blog', __name__)

# Other routes...

# Update a post (Handle both GET for rendering and POST for updating)
@blog.route('/posts/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        data = request.form  # Get data from the form
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return render_template('index.html', posts=Post.query.all())  # Redirect to the updated posts
    return render_template('edit_post.html', post=post)  # Optionally, render an edit form
