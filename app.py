from flask import Flask 
from flask_restful import Api, Resource
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
api = Api(app)

#  MySQL connection
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ace"
)

class ApiHandler(Resource):
    def get(self):
        # Executing the MySQL query
        cursor = mysql_connection.cursor()
        cursor.execute("SELECT `ID`,`Questions`,`Answers` FROM `ace`")
        rows = cursor.fetchall()
        cursor.close()

        # Formating the result
        results = []
        for row in rows:
            results.append({
                'id': row[0],
                'Question': row[1],  
                'Answers': row[2]         
            })

        return {
            'resultstatus': 'SUCCESS',
            'message': "Hello Api Handler.py",
            'data': results
            }
    
api.add_resource(ApiHandler, '/flask')

if __name__ == '__main__':
    app.run(debug=True)
