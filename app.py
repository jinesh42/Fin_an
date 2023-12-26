from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/') 
#@app.route('/home')
def index():
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=False)