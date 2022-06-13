import sqlite3

base = "database.db"
class DataBase:
    def getBaseID(self,id):  # id bazada bormi yoki yuq shuni tekshirishda yordam beradi
        try:
            connation = sqlite3.connect(base)
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM main WHERE userID = {id}")
            a = cursor.fetchall()
            return a
        except Exception as e:
            print(e)
    def getBasa(self):    # Bazadagi barcha malumotlarni olish
        try:
            connation = sqlite3.connect(base)
            cursor = connation.cursor()
            cursor.execute("SELECT * FROM main")
            return cursor.fetchall()

        except Exception as e:
            print(e)
    def getBasaID(self):    # Bazadagi barcha IDlar
        try:
            connation = sqlite3.connect(base)
            cursor = connation.cursor()
            cursor.execute("SELECT userID FROM main")
            return cursor.fetchall()

        except Exception as e:
            print(e)
    def setBase(self,userN,firstN,date,ID):
        try:
            connation = sqlite3.connect(base)
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO main(user_name,first_name,date,userID) VALUES('{userN}','{firstN}','{date}',{ID})")
            connation.commit()
            connation.close()
        except Exception as e:
            print(e)