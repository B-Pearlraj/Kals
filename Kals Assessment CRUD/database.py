import sqlite3

class Database:
    def __init__(self, db):
        try:
            self.con = sqlite3.connect(db)
            self.c = self.con.cursor()
            self.c.execute("""
                CREATE TABLE IF NOT EXISTS datas(
                    pid INTEGER PRIMARY KEY,
                    ProductName TEXT NOT NULL,
                    ProductSaleDate INTEGER NOT NULL,
                    Quantity INTEGER NOT NULL,
                    Price INTEGER NOT NULL
                    )
                """)
            self.con.commit()
            print("Table Created Successfully")
        except Exception as e:
            print("Error:", e)

    def insert_record(self):
        name = input("Enter Your ProductName:")
        date = input("Enter Your Sale DATE:")
        quantity = input("Enter Product Quantity:")
        price = input("Enter Price:")
        sql = """
                INSERT INTO datas VALUES(NULL,?,?,?,?)
            """
        self.c.execute(sql, (name, date, quantity, price))
        self.con.commit()
        print("Record Added Successfully")

    def fetch_record(self):
        self.c.execute("SELECT * FROM datas")
        data = self.c.fetchall()
        print("\n")
        print("List of Records")
        print("---------------")
        for datas in data:
            print(datas)

    def update_record(self):
        print("1.Product Name")
        print("2.Sale Date")
        print("3.Quantity")
        print("4.Price")
        option = int(input("\nWhich field you want to update?:"))
        if option == 1:
            pid = input("Enter Product ID:")
            name = input("Enter Product Name:")
            sql = """ UPDATE datas set ProductName=? where pid=?"""
            self.c.execute(sql, (name, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 2:
            pid = input("Enter Product ID:")
            date = input("Enter Sale Date:")
            sql = """ UPDATE datas set SaleDate=? where pid=?"""
            self.c.execute(sql, (date, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 3:
            pid = input("Enter Product ID:")
            quantity = input("Enter Quantity:")
            sql = """ UPDATE datas set Quantity=? where pid=?"""
            self.c.execute(sql, (quantity, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        elif option == 4:
            pid = input("Enter Product ID:")
            price = input("Enter Price:")
            sql = """ UPDATE datas set Price=? where pid=?"""
            self.c.execute(sql, (price, pid))
            self.con.commit()
            obj.fetch_record()
            print("\n")
            print("Update Successfully")
        else:
            print("Invalid")

    def remove_record(self):
        pid = input("Enter Your ID:")
        sql = "DELETE FROM datas WHERE pid=?"
        self.c.execute(sql, (pid,))
        self.con.commit()
        obj.fetch_record()
        print("\n")
        print("Record Deleted Successfully")


obj=Database("Sqlitedatabase.db")

while True:
    print("\n")
    print("1 :Insert Record")
    print("2 :Fetch Record")
    print("3 :Update Record")
    print("4 :Delete Record")

    print("\n")

    option = int(input("Please Enter Your Operation:"))

    if option == 1:
        obj.insert_record()
    elif option == 2:
        obj.fetch_record()
    elif option == 3:
        obj.update_record()
    elif option == 4:
        obj.remove_record()
    else:
        quit()