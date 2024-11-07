from app import app, db, User

def add_user(userID, password, role):
    new_user = User(userID=userID, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    print(f'User {userID} added successfully!')

if __name__ == '__main__':
    with app.app_context():
        add_user('dr1', 'pdr1', 'Department Representative')
        add_user('dr2', 'pdr2', 'Department Representative')
        add_user('dr3', 'pdr3', 'Department Representative')
        add_user('c1', 'pc1', 'Contractor')
        add_user('c2', 'pc2', 'Contractor')
        add_user('c3', 'pc3', 'Contractor')
        add_user('a1', 'pa1', 'Admin')