from app import db
from models import User, Post

# Create the database tables
def work():
    db.create_all()