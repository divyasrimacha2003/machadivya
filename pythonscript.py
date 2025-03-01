from flask import Flask, request, redirect, render_template_string
import mysql.connector

app = Flask(_name_)
conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="your_database")
cursor = conn.cursor(dictionary=True)

index_html = '''<html><head><title>Employees</title></head><body><h1>Employees</h1><table border="1"><tr><th>ID</th><th>Name</th><th>Email</th><th>Actions</th></tr>{% for emp in employees %}<tr><td>{{ emp.employee_id }}</td><td>{{ emp.name }}</td><td>{{ emp.email }}</td><td><a href="/edit/{{ emp.employee_id }}">Edit</a> <a href="/delete/{{ emp.employee_id }}">Delete</a></td></tr>{% endfor %}</table><br><a href="/add">Add New Employee</a></body></html>'''
add_html = '''<html><head><title>Add Employee</title></head><body><h1>Add Employee</h1><form method="post">Name: <input type="text" name="name"><br>Email: <input type="email" name="email"><br><input type="submit" value="Add"></form></body></html>'''
edit_html = '''<html><head><title>Edit Employee</title></head><body><h1>Edit Employee</h1><form method="post">Name: <input type="text" name="name" value="{{ employee.name }}"><br>Email: <input type="email" name="email" value="{{ employee.email }}"><br><input type="submit" value="Update"></form></body></html>'''

@app.route('/')
def index():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template_string(index_html, employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("INSERT INTO employees (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        return redirect('/')
    return render_template_string(add_html)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("UPDATE employees SET name=%s, email=%s WHERE employee_id=%s", (name, email, id))
        conn.commit()
        return redirect('/')
    cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (id,))
    employee = cursor.fetchone()
    return render_template_string(edit_html, employee=employee)

@app.route('/delete/<int:id>')
def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (id,))
    conn.commit()
    return redirect('/')

if _name_ == '_main_':
    app.run(debug=True)