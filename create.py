
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

from flask import Flask, jsonify, render_template, request
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
    # this line of code commit changes to the database and close the connection
    mysql.connection.commit()
    dbConn.close()
    return jsonify({"message": "Table created successfully"}), 201




#this line of code help to drop database
@server.route("/dropdatabase", methods=["POST"])
def drop_database():
    db_name = 'doshmydb'  # Replace with the name of the database you want to drop
    db_conn = mysql.connection.cursor()
    db_conn.execute("DROP DATABASE IF EXISTS %(db_name)s", {"db_name": db_name}) #to prevent sql injectiomn attack
    mysql.connection.commit()
    db_conn.close()

    return jsonify({"message": f"Database '{db_name}' dropped successfully"}), 200


#this line of code help you trancate a table 
@server.route("/truncatedatabase/{table_name}", methods=["POST"])
def truncate_database():
    db_name = 'doshmydb'
    db_conn = mysql.connection.cursor()
    
    # Fetch all table names in the database
    db_conn.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{db_name}'")
    tables = db_conn.fetchall()
    
    # Truncate each table
    for table in tables:
        table_name = table[0]
        db_conn.execute(f"TRUNCATE TABLE {table_name}")
    
    mysql.connection.commit()
    db_conn.close()
    
    return jsonify({"message": f"All tables in database '{db_name}' truncated successfully"}), 200


# this line of code helps to rollback  transactiom
@server.route("/rollback", methods=["POST"])
def rollbackExample():
    dbConn = mysql.connection.cursor()
    dbConn.execute("START TRANSACTION")

    # Perform some operations
    dbConn.execute("INSERT INTO sallah (fname, lname, email, password) VALUES (%s, %s, %s, %s)", 
                   ('ade', 'monday', 'ademon@gmail.com', 'wicki44'))

    # Intentionally cause an error to trigger a rollback
    dbConn.execute("INSERT INTO maydb (value) VALUES ('test')")

    # Commit the transaction if everything goes well
    mysql.connection.commit()
    dbConn.close()

    return jsonify({"message": "Transaction successful"}), 201


# this line of code help you drop table
@server.route("/droptable", methods=["POST"])
def dropTable():
    table_name = request.json.get('sallah')

    if not table_name:
        return jsonify({"error": "Table name is required"}), 400

    dbConn = mysql.connection.cursor()
    dbConn.execute(f"DROP TABLE IF EXISTS {table_name}")
    mysql.connection.commit()
    dbConn.close()

    return jsonify({"message": f"Table '{table_name}' dropped successfully"}), 200



@server.route("/register", methods=["POST"])
def regUser():
    data = request.json
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['password']

    dbConn = mysql.connection.cursor()

    #this line of code starts a transaction  
    dbConn.execute("START TRANSACTION")

    #this line of code Execute the insert query
    dbConn.execute("INSERT INTO sallah (fname, lname, email, password) VALUES (%s, %s, %s, %s)", 
                   (fname, lname, email, password))
    
    # commits the transaction
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


@server.route("/homemy", methods=["GET"])
def Homepage_r():
    return render_template("home.html")


if __name__ == '__main__':
    server.run(debug=True, port=5001)
