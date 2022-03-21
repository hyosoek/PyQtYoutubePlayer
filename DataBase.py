import sqlite3

class DataBase:
    def __init__(self):
        self.con = None 
        self.cur = None 
        self.connectDataBase()
        self.createTable()
        
    def connectDataBase(self): 
        self.con = sqlite3.connect("UserDataBase.db")
        self.cur = self.con.cursor() 

    #묶기
    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (id TEXT, pw TEXT, name TEXT, usercode INTEGER PRIMARY KEY AUTOINCREMENT)") #대소문자 구분하기
        self.cur.execute("CREATE TABLE IF NOT EXISTS playlist (usercode INTEGER, playlistname TEXT, playlistcode INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY(usercode) REFERENCES user(usercode))") #fk가 pk가 되면 안됨
        self.cur.execute("CREATE TABLE IF NOT EXISTS video (playlistcode INTEGER, url TEXT, videocode INTEGER PRIMARY KEY AUTOINCREMENT, FOREIGN KEY(playlistcode) REFERENCES playlist(playlistcode))") #fk가 pk가 되면 안됨
        self.cur.execute("PRAGMA foreign_keys = 1")

    def dataCreate(self,tableName,columnList,dataList):
        sentence = "INSERT INTO "
        sentence += tableName
        sentence += "("
        for i in range(0,len(columnList)-1):
            sentence += columnList[i]
            sentence += ", "
        sentence += columnList[len(columnList)-1]
        sentence += ") VALUES("
        for i in range(0,len(columnList)-1):
            sentence += "?"
            sentence += ", "
        sentence += "?"
        sentence += ")"
        data = dataList
        self.cur.execute(sentence,data) 
        self.con.commit()
        
    def dataRead(self,tableName,dataCol,data):
        sentence = "SELECT * FROM "
        sentence += str(tableName)
        sentence += " WHERE "
        sentence += str(dataCol)
        sentence += "=?"
        dataArr = [data]
        self.cur.execute(sentence,dataArr) 
        result = self.cur.fetchall() 
        return result

    def dataUpdate(self,tableName,colType,newData,usercode): #중복체크
        sentence = "UPDATE "
        sentence += tableName
        sentence += " SET "
        sentence += colType
        sentence += "=? WHERE usercode=?"
        data = [newData,usercode]
        self.cur.execute(sentence,data) 
        self.con.commit()
    
    def dataDelete(self,tableName,colName,data): #아이디 로그인 체크
        sentence = "DELETE FROM "
        sentence += tableName
        sentence += " WHERE "
        sentence += colName
        sentence += "=?"
        dataList = [data]
        self.cur.execute(sentence,dataList) 
        self.con.commit()