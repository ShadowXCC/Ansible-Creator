from flask import Flask, render_template, redirect, url_for, request, flash, session
#from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'mysecretkey'
#db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        # new_user = User(username=username, email=email, password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()
        flash('You have successfully registered')
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # user = User.query.filter_by(username=username).first()
        # if user and check_password_hash(user.password, password):
        #     session['user_id'] = user.id
        #     session['username'] = user.username
        #     flash('You have successfully logged in')
        #     return redirect(url_for('index'))
        # else:
        #     flash('Invalid username or password')
        #     return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have successfully logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)