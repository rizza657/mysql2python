
# from flask import Flask, jsonify, request
# from flask_mysqldb import MySQL
# server = Flask(__name__) 
# server.config["MySQL_HOST"] = "localhost",
# server.config["MySQL_USER"] = "root",
# server.config["MySQL_PASSWORD"] = " ",
# server.config["MYSQL_DB"] = "doshmydb"

# mysql = MySQL(server)

# @server.route("/", methods=["GET"])
# def homepage():
#      if(request.method == "GET"):
#          return jsonify({
#              "message":"welcome",
#              "type":"success"
#          })
#      return "could not load page"




# # server = Flask(__name__) 
# # @server.route("/home", methods=["GET", "POST"])
# # def homepage():
# #     if(request.method == "GET"):
# #         return jsonify({
# #             "message":"welcome",
# #             "type":"success"
# #         })
# #     return "could not load page"
# @server.route("/databaseset", methods=["POST"])
# def createDB():
#     dbConn = mysql.connection.cursor() 
#     if dbConn:
#         dbConn.execute(f"""CREATE TABLE IF NOT EXISTS `doshmydb`(
#                                 `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#                                 `fname` VARCHAR(50),
#                                 `lname` VARCHAR(50),
#                                 `email` VARCHAR(50),
#                                 `password` VARCHAR(50)
#             ) 
#         """)
#         mysql.connection.commit()
#         return jsonify({"message": "Table created successfully"}), 201
#     return jsonify({"message": "Could not create table"}), 500




# @server.route("/register", methods=["POST"])
# def regUser():
#     try:
#         id = request.json['id']
#         fname = request.json['fname']
#         lname = request.json['lname']
#         email = request.json['email']
#         password = request.json['password']

#         dbConn = mysql.connection.cursor()
#         dbConn.execute("INSERT INTO doshmydb (id, fname, lname, email, password) VALUES (%s, %s, %s, %s, %s)", (1, 'ademola', 'sunday', 'ademolas@gmail.com', 'sunsun09'))
#         mysql.connection.commit()
#         dbConn.close()







#     # return jsonify({
#     #     "id": id,
#     #     "fname": fname,
#     #     "lname": lname,
#     #     "email": email,
#     #     "password": password
#     # })

#     # if not all([fname, lname, email, password]):
#     #     return jsonify({"error": "Missing data"}), 400




#         return jsonify({
#             "message": "User registered successfully",
#             "type": "success",
#             "id": 1,
#             "fname": "admola",
#             "lname": "sunday",
#             "email": "ademolas@gmail.com",
#             "password": "sunsun09"
#         }), 
    
    
# if(__name__ == '__main__'):
#     server.run(debug=True)




#     server = Flask(__name__) 
# @server.route("/", methods=["GET"])
# def homepage():
#     if(request.method == "GET"):
#         return jsonify({
#             "message":"welcome",
#             "type":"success"
#         })
#     return "could not load page"

# string = ['mark', 'jessica', 'mandy']

# def add_s():
#     strings = [s + 's' for s in string]  # Add 's' to each string in the list
#     print(strings)

# add_s()  # Call the function to print the updated list

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb



# Database connection details
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "doshmydb"

# Connect to the database
db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
cursor = db.cursor()

# Create the `users` table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sallah (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        fname VARCHAR(50),
        lname VARCHAR(50),
        email VARCHAR(50),
        password VARCHAR(50)
    )
""")

# Commit changes and close the connection
db.commit()
cursor.close()
db.close()

print("Table 'sallah' created or already exists.")

server = Flask(__name__)
server.config["MYSQL_HOST"] = "localhost"
server.config["MYSQL_USER"] = "root"
server.config["MYSQL_PASSWORD"] = ""
server.config["MYSQL_DB"] = "doshmydb"

mysql = MySQL(server)

@server.route("/", methods=["GET"])
def homepage():
    return jsonify({
        "message": "welcome",
        "type": "success"
    })

@server.route("/databaseset", methods=["POST"])
def createDB():
    dbConn = mysql.connection.cursor()
    dbConn.execute("""
        CREATE TABLE IF NOT EXISTS sallah (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            fname VARCHAR(50),
            lname VARCHAR(50),
            email VARCHAR(50),
            password VARCHAR(50)
        )
    """)
    mysql.connection.commit()
    dbConn.close()
    return jsonify({"message": "Table created successfully"}), 201

@server.route("/register", methods=["POST"])
def regUser():
    data = request.json
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['password']

    dbConn = mysql.connection.cursor()
    dbConn.execute("INSERT INTO sallah (fname, lname, email, password) VALUES (%s, %s, %s, %s)", 
                   (fname, lname, email, password))
    mysql.connection.commit()
    dbConn.close()

    return jsonify({
        "message": "User registered successfully",
        "type": "success",
        "fname": fname,
        "lname": lname,
        "email": email,
        "password": password
    }), 201

if __name__ == '__main__':
    server.run(debug=True, port=5001)
