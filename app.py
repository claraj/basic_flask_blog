from flask import Flask, request, render_template, session, redirect, url_for
import uuid 
import db 
from model import Post

app = Flask(__name__)
app.secret_key = 'serjse094tus90efjxoidvnxo;ifjbn' # TODO longer complicated key and keep it secret


@app.before_request
def ensure_session_id():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())


@app.route('/')
def homepage():
    # show list of posts for user 
    user_id = session['session_id']
    posts = db.get_all_posts_for_user(user_id)
    return render_template('home.html', posts=posts)


@app.route('/create-new-post')
def create_new_blog_post_form():
    # Display form to enter new post 
    return render_template('new_post.html')


@app.route('/submit-new-post', methods=['POST'])
def submit_new_blog_post():
    # receive new post form submission 
    user_id = session['session_id']
    form_data = request.form.to_dict() 
    post = Post(user_id, form_data['title'], form_data['text'])
    db.new_post(post)
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)