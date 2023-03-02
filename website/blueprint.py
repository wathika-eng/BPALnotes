from flask import Blueprint, render_template, request

posts = Blueprint('views', __name__)


#@views.route('/search')
#def post_list():
#    q = request.args.get('q')
#    if q:
#        posts = views.query.filter(Post.title.contains(q) |
#                Post.body.contains(q))
#        else: 
#        posts = Post.query.all()
#        return render_template('base.html', posts=posts)
