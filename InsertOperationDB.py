import mysql.connector as connector

class DBConnection2:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='pythoncruddb'
        )
        query = 'create table if not exists Student(id int primary key, name varchar(20) not null, phone float)'
        cur = self.con.cursor()
        cur.execute(query)
        print("Table created successfully !")

    # insert
    def insert_student(self,id,name,phone):
            query = "insert into Student(id,name,phone) values({},'{}','{}')".format(id,name,phone)

            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Student Inserted Successfully ! ")


# main mathod
dbhelper = DBConnection2()
dbhelper.insert_student(103,"ritesh",9699545454)
dbhelper.insert_student(104,"umesh",9699545454)
dbhelper.insert_student(105,"ishwar",9699545454)
