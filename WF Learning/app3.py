from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# create Flask app
app = Flask(__name__)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create database object
db = SQLAlchemy(app)

# create model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# create route to add user to database
@app.route('/users', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return 'User created successfully!'

# create route to display all users from database
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    # create database tables
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
