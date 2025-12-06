import mysql.connector as connector

class DBConnection:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='pythoncruddb'
        )

        query = "create table if not exists Student(id int primary key, name varchar(20), phone float)"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table created Successfully !!")

# main function
dbhelper = DBConnection()
