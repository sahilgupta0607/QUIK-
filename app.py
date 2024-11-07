from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy import text
from database import engine
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userId']
        password = request.form['password']
        user_role = request.form['userRole']

        with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM Users WHERE userID = :user_id'), {'user_id': user_id})
            user = result.fetchone()  

        if user:
            db_user_id = user[0]   
            db_password = user[1]  
            db_user_role = user[2] 

            if db_user_id == user_id and db_password == password and db_user_role == user_role:
                if user_role == 'Department Representative':
                    return redirect(url_for('department_representative_actions'))
                elif user_role == 'Contractor':
                    return redirect(url_for('contractor_actions'))
                elif user_role == 'Admin':
                    return redirect(url_for('admin_actions'))
        
        flash('User does not exist, please check your credentials.')
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/add_project', methods=['POST'])
def add_project():
    if 'user_id' not in session:
        flash('You must be logged in to add a project.')
        return redirect(url_for('login'))

    user_id = session['user_id']  # Retrieve the logged-in user's ID (Department Representative ID)

    project_data = {
        'ID': request.form['projectId'],
        'Name': request.form['projectName'],
        'SDate': request.form['projectDate'],
        'EDate': request.form['completionDate'],
        'Budget': request.form['projectAmount'],
        'CID': request.form['contractorId'],
        'State': request.form['projectLocation'],
        'District': request.form['projectDistrict'],
        'CityTown': request.form['projectCity'],
        'Pincode': request.form['projectPincode'],
        'Status': request.form['projectStatus'],
        'Details': request.form['projectDetail'],
        'DRID': user_id
    }

    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM Projects WHERE ID = :ID'), {'ID': project_data['ID']})
            existing_project = result.fetchone()

            if existing_project:
                flash('Project ID already exists. Please use a unique ID.')
                return redirect(url_for('department_representative_actions'))

            conn.execute(text('''
                INSERT INTO Projects (ID, Name, SDate, EDate, Budget, CID, State, District, CityTown, Pincode, Status, Details, DRID)
                VALUES (:ID, :Name, :SDate, :EDate, :Budget, :CID, :State, :District, :CityTown, :Pincode, :Status, :Details, :DRID)
            '''), **project_data) 

        flash('Project added successfully!')
    except Exception as e:
        flash(f'An error occurred while adding the project: {str(e)}')
    
    return redirect(url_for('department_representative_actions'))

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
