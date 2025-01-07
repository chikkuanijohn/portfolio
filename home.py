from flask import Flask,render_template,redirect,request,url_for
app=Flask(__name__)
import sqlite3

con = sqlite3.connect('data.db') 
try:
    con.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            email  TEXT NOT NULL,
            msg  TEXT NOT NULL
        )
    ''')
except:
    pass    

@app.route('/')
def fun1():
    return render_template('index.html')




@app.route('/index',methods=['POST'])
def fun2():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        msg=request.form['Message']

        con = sqlite3.connect('data.db')
        con.execute('INSERT INTO users (name,email,msg) VALUES (?,?,?,?)', (name,email,msg))
        con.commit()
        con.close()
        print(name,email,msg)
        return redirect(url_for('fun1'))

app.run()