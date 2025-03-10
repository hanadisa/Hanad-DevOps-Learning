# app.py

from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="mydb",    # Hostname of the MySQL container
        user="root",    # Username to connect to MySQL
        passwd="my-secret-pw",  # Password for the MySQL user
        db="mysql"      # Name of the database to connect to
    )
    cur = db.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()
    return f'Hello, World! MySQL version: {version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)