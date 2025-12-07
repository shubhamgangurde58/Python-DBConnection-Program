import mysql.connector as connector 

class DBConnection4:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='pythoncruddb'
        )
        print("Get Connection Successfully ! ")
        cur = self.con.cursor()
        query = "create table if not exists Employee(id int primary key , name varchar(20), address varchar(20))"
        cur.execute(query)
        print("Table Created Successfully ! ")

    # insert 
    def insert_Employee(self, id, name, address):
        cur = self.con.cursor()
        query = "insert into Employee(id,name,address) values({},'{}','{}')".format(id,name,address)
        cur.execute(query)
        self.con.commit()
        print("Employee Inserted Successfully ! ")

    # Show All Employee 
    def showAll_Employee(self):
        cur = self.con.cursor()
        query = "select * from Employee"
        cur.execute(query)
        for row in cur:
            print("ID = ",row[0])
            print("Name = ",row[1])
            print("Address = ",row[2])
            print("--------------------------")

    # Delete Employee using id :
    def delete_Employee(self, id):
        cur = self.con.cursor()
        query = "delete from employee where id = {}".format(id)
        cur.execute(query)
        self.con.commit()
        print("Employee Deleted Successfully !")

    # Update Employee Info Using id  
    def update_Employee(self, id, name , address):
        cur = self.con.cursor()
        query = "update Employee SET name = '{}', address = '{}' where id = {}".format(name,address,id)
        cur.execute(query)
        self.con.commit()
        print("Employee Info Updated ! ")
        

# main Method 
dbhelper = DBConnection4()
# dbhelper.insert_Employee(101,'shubham','sawkheda')
# dbhelper.insert_Employee(102,'jayesh','khetiya')
# dbhelper.insert_Employee(103,'ritesh','deur')
# dbhelper.insert_Employee(104,'umesh','shelti')
# dbhelper.insert_Employee(105,'ishwar','shahada')

# dbhelper.showAll_Employee()
# dbhelper.delete_Employee(104)
# dbhelper.showAll_Employee()

dbhelper.update_Employee(101,'rushi','nandurbar')
        
        