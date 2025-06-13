from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/utilisateurs')
def utilisateurs():
    conn = mysql.connector.connect(
        host='mysql',
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Utilisateurs")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
