from app import app, db, Users

with app.app_context():
    db.create_all()

