from flask import Flask, jsonify, request
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
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

# create route to get all users from database
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        result.append(user_data)
    return jsonify(result)

if __name__ == '__main__':
    # create database tables
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
