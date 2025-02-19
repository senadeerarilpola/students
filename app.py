from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        grade TEXT NOT NULL)''')
    conn.commit()
    conn.close()


# Route to display the home page
@app.route('/')
def index():
    return render_template('index.html')


# Route to display the form to add a new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        conn.close()

        return redirect(url_for('view_students'))
    return render_template('add_student.html')


# Route to display the list of students
@app.route('/view')
def view_students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('view_students.html', students=students)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)