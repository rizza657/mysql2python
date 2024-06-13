
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
server = Flask(__name__) 
server.config["MySQL_HOST"] = "localhost",
server.config["MySQL_USER"] = "root",
server.config["MySQL_PASSWORD"] = " ",
mysql = MySQL(server)
@server.route("/", methods=["GET"])
def homepage():
     if(request.method == "GET"):
         return jsonify({
             "message":"welcome",
             "type":"success"
         })
     return "could not load page"




# server = Flask(__name__) 
# @server.route("/home", methods=["GET", "POST"])
# def homepage():
#     if(request.method == "GET"):
#         return jsonify({
#             "message":"welcome",
#             "type":"success"
#         })
#     return "could not load page"
@server.route("/databaseset", methods=["POST"])
def createDB():
    dbConn = mysql.connection.cursor() 
    if(dbConn):
        dbConn = dbConn.execute(f"""CREATE TABLE IF NOT EXISTS `doshmydb`(
                                `id` int not null primary key auto_increment,
                                `fname` VARCHAR(50)
                                `lname` VARCHAR(50)
                                `email` VARCHAR(50)
                                `password` VARCHAR(50)
                                )""")
        mysql.connection.commit()
@server.route("/register", methods=["POST"])
def regUser():
    fname = request.json['fname']
    password = request.json['password']
    return jsonify({
        "fname":fname,
        "password":password
    })
    
if(__name__ == '__main__'):
    server.run(debug=True)




#     server = Flask(__name__) 
# @server.route("/", methods=["GET"])
# def homepage():
#     if(request.method == "GET"):
#         return jsonify({
#             "message":"welcome",
#             "type":"success"
#         })
#     return "could not load page"