# Imports
from database import Database
from flask import jsonify, request
import hashlib

class Login:
    # Class init
    def __init__(self):
        self.db = Database()
        self.wrongLogin = "Neispravna email adresa ili lozinka. Pokušajte ponovo."

    # Check login
    def checkLogin(self, email, password):
        db = self.db.connectDB()
        cursor = db.cursor()
        
        sql = "SELECT u.id, u.usertype, ut.typename, u.name, u.email FROM users u JOIN usertype ut ON u.usertype = ut.id WHERE u.email = ? AND password = ?"
        cursor.execute(sql, [email, password])
        data = cursor.fetchone()        

        if data:
            sql = "INSERT INTO login (userid) VALUES (?)"
            cursor.execute(sql, [data[0]])
            db.commit()

        db.close()
        
        return data

    # Get all
    def getAll(self):
        db = self.db.connectDB()
        cursor = db.cursor()

        sql = "SELECT u.id, u.usertype, ut.typename, u.name, u.email, l.logindate FROM users u JOIN usertype ut ON u.usertype = ut.id JOIN login l ON u.id = l.userid ORDER BY logindate DESC"
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return data

    # Get last hour
    def getLastHour(self):
        db = self.db.connectDB()
        cursor = db.cursor()

        sql = "SELECT u.id, u.usertype, ut.typename, u.name, u.email, MAX(DATETIME(l.logindate)) FROM users u JOIN usertype ut ON u.usertype = ut.id JOIN login l ON u.id = l.userid WHERE DATETIME(l.logindate) >= DATETIME('NOW', '-1 Hour') AND u.usertype = 1  GROUP BY u.id, u.usertype, ut.typename, u.name, u.email ORDER BY logindate DESC"
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return data

    ################ ENDPOINTS Methods #####################
    # Check login
    def epcheckLogin(self):
        details = request.get_json()
        email = details["email"]
        password = details["password"];

        Password = hashlib.md5()
        Password.update(password.encode("utf-8"))
        password = Password.hexdigest()

        result = self.checkLogin(email, password)
        if not result:
            return jsonify({"msg": self.wrongLogin})
 
        return jsonify({"id": result[0], "usertype": result[1], "typename": result[2], "name": result[3], "email": result[4]})

    # Get all
    def epGetAll(self):
        data = self.getAll()

        items = []
        for item in data:
            items.append({"id": item[0], "usertype": item[1], "typename": item[2], "name": item[3], "email": item[4], "logindate": item[5]})
    
        return jsonify({"logins": items})

    # Get last hour
    def epGetLastHour(self):
        data = self.getLastHour()

        items = []
        for item in data:
            items.append({"id": item[0], "usertype": item[1], "typename": item[2], "name": item[3], "email": item[4], "logindate": item[5]})
    
        return jsonify({"logins": items})