import mysql.connector as connector

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='root',
                        database='pythoncruddb')

print("Get Connection Successfully !")

query = 'create table if not exists Student(id int primary key, name varchar(20) not null, phone float)'
cur = con.cursor()
cur.execute(query)

print("Table Created Successfully !")
