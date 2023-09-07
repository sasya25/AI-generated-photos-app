from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from .image_generator import ImageGenerator
from .feed_generator import FeedGenerator
from .models import User
from flask import current_app as app
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    feed_generator = FeedGenerator(1)
    return render_template('index.html', photos=feed_generator.get_feed(100))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
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

@app.route('/generate_form')
@login_required
def generate_form():
    return render_template('image_generation.html')

@app.route('/generate_image', methods=['POST'])
@login_required
def generate_image_endpoint():
    try:
        text = request.json.get('text')
        if text:
            image_generator = ImageGenerator()
            generated_image_url = image_generator.generate_image(text)
            return jsonify({"image_url": generated_image_url})
        else:
            return jsonify({"error": "Missing 'text' parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/post_image', methods=['POST'])
@login_required
def post_image():
    try:
        # In a real-world scenario, you would store the image URL in a database or perform further processing.
        received_image_url = request.json.get('imageUrl')
        
        # You can now use received_image_url as needed, e.g., store it in a database.
        
        return jsonify({"message": "Image URL received and processed successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

