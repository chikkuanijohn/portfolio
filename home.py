from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Store data in the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contact (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        message TEXT NOT NULL)''')
    cursor.execute("INSERT INTO contact (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return redirect('/data')

@app.route('/data')
def view_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contact")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
