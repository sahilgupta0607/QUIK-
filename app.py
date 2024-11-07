from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Absolute path to the current directory
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "project.db")}'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a User model
class User(db.Model):
    userID = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))

    def __repr__(self):
        return f'<User {[self.userID, self.password, self.role]}>'
    


# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userId']
        password = request.form['password']
        user_role = request.form['userRole']

        # Query the database to find the user
        user = User.query.filter_by(userID=user_id, password=password, role=user_role).first()
        
        if user:
            # Redirect to role-specific actions page based on user role
            if user.role == 'Department Representative':
                return redirect(url_for('department_representative_actions'))
            elif user.role == 'Contractor':
                return redirect(url_for('contractor_actions'))
            elif user.role == 'Admin':
                return redirect(url_for('admin_actions'))
        else:
            # Flash an error message if user is not found
            flash('User does not exist, please check your credentials.')
            return redirect(url_for('login'))
    
    return render_template('index.html')

# Role-specific action pages
@app.route('/department_representative/actions')
def department_representative_actions():
    return render_template('drActions.html')

@app.route('/contractor/actions')
def contractor_actions():
    return render_template('cActions.html')

@app.route('/admin/actions')
def admin_actions():
    return render_template('aActions.html')

if __name__ == '__main__':
    app.run(debug=True)
