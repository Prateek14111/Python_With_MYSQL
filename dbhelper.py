import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Pragya@3103',database='pythontest')
        query='create table if not exists user(userID int primary key,userName varchar(200),phone varchar(20))'
        cur=self.con.cursor()
        cur.execute(query)
        print("created")
    
    def insert_data(self, userid, name, phone):
         insertquery = "insert into user(UserID,userName,phoneNumber)value({},'{}','{}')".format(
            userid, name, phone)
        cursor = self.con.cursor()
        cursor.execute(insertquery)
        self.con.commit()
        print('user saved to database')
# fetchall function

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            my_format = "ID:{} NAME: {} PHONE:{}"
            print(my_format.format(row[0], row[1], row[2]))
# fetch_id function

    def fetch_id(self):
        query = "select UserID from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            format = "UserID:{}"
            print(format(row[0]))

# delete function
    def delete_record(self, _userid):
        query = "delete from user where UserID={}".format(_userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("record deleted")

# update function
    def update_record(self, _userid, new_name, new_phone):
        query = "update user set userName='{}',phoneNumber='{}' where UserID={}".format(
            new_name, new_phone, _userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("record updated")
