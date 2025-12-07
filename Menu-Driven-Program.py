import mysql.connector as connector

class Menu_Driven_Program:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='pythoncruddb'
        )
        cur = self.con.cursor()
        query = 'create table if not exists EmployeeInfo(Eid int primary key , Name varchar(20) , address varchar(20))'
        cur.execute(query)
        print("Table Created Successfully ! ")

    # insert Record
    def insert_Employee(self,eid, name, address):
        cur = self.con.cursor()
        query = "insert into EmployeeInfo(eid, name , address) values({},'{}','{}')".format(eid,name,address)
        cur.execute(query)
        self.con.commit()
        print("Record  Inserted Successfully ! ")

    # Fetch Record 
    def show_AllRecord(self):
        cur = self.con.cursor()
        query ="select * from EmployeeInfo"
        cur.execute(query)
        print("\n------ All Employees ------")
        for row in cur:
            print("Eid:", row[0], " | Name:", row[1], " | Address:", row[2])
        print("------------------------------")
    
    # Delete Record
    def Delete_Employee(self,eid):
        cur = self.con.cursor()
        query = "delete from EmployeeInfo where eid = {}".format(eid)
        cur.execute(query)
        self.con.commit()
        print("Employee Deleted Successfully ! ")

    def Update_Employee(self,eid,name,address):
        cur = self.con.cursor()
        query = "update EmployeeInfo SET  name = '{}', address = '{}' where eid = {}".format(name,address,eid)
        cur.execute(query)
        self.con.commit()
        print("Employee Updated Successfully !")


# main  function
def main():
    
    dbhelper = Menu_Driven_Program()

    while True:

        print("\n\t********* Welcome To Menu Driven System *********\n")
        print("\n======== MENU ========\n")
        print("1. AddEmployee")
        print("2. ShowAllEmployee")
        print("3. DeleteEmployee")
        print("4. UpdateEmployee")
        print("5. Exit")

        choice = int(input("\nEnter your Choice : "))

        match choice:
        
            case 1:
                eid = int(input("Enter Id: "))
                name = input("Enter Name: ")
                address = input("Enter Address: ")
                dbhelper.insert_Employee(eid,name,address)
            case 2:
                dbhelper.show_AllRecord()
            case 3: 
                eid = int(input("Enter ID to Delete: "))
                dbhelper.Delete_Employee(eid)
            case 4: 
                eid = int(input("Enter ID to Update: "))
                name = input("Enter New Name: ")
                address = input("Enter New Address: ")
                dbhelper.Update_Employee(eid,name,address)
            case 5:
                print("Thank you! Exiting Program...")
                break
            case _:
                print("Invalid Input !")


# Call Main 
main()