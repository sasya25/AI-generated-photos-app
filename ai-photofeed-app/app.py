from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
login_manager = LoginManager()
login_manager.init_app(app)

# Mock user data (replace with your own user database)
users = {
    'user1': {'username': 'a', 'password': 'a'},
    'user2': {'username': 'user2', 'password': 'password2'}
}

# Sample photos (you can replace these with your own photo URLs)
photos = [
    {"id": 1, "url": "/static/images/photo1.jpg", "caption": "Beautiful sunset"},
    {"id": 2, "url": "/static/images/photo2.jpg", "caption": "Exploring the mountains"},
    {"id": 3, "url": "/static/images/photo3.jpg", "caption": "City lights at night"},
]

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
@login_required
def index():
    return render_template('index.html', photos=photos)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            user_obj = User(username)
            login_user(user_obj)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))

        flash('Login failed. Please check your username and password.', 'danger')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

