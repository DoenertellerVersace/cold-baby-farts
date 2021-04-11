import sqlite3
from sqlite3 import Error
import datetime


class DB_Provider:

    def create_connection(self, path):
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
            return connection
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_query(self, conn, query):
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def query_return(self, conn, sel, fro, whe):
        cursor = conn.cursor()
        try:
            print(f"SELECT {sel} FROM {fro} WHERE {whe};")
            cursor.execute(f"SELECT {sel} FROM {fro} WHERE {whe};")
            rows = cursor.fetchall()
            print(f"Operation successfully executed on {fro}!")
            print
            return rows
        except Error as e:
            print(e)
            return None

    def show_next(self, devices, area):
        lst = devices
        print(lst)
        lst.sort(key=lambda x: x[2])
        n_lst = []
        for element in lst:
            date = datetime.datetime.strptime(element[2], '%Y-%m-%d %H:%M:%S')
            diff = date - datetime.datetime.now()
            if diff.days <= area:
                n_lst.append(element)
        n_lst.reverse()
        return n_lst

    def getList(self):
        conn = self.create_connection("../pcdrdata.sqlite3")

        sel = "IDNumber, DeviceDescription, NextTest"
        fro = "tblIDNumbers"
        whe = "TestResult = 'OK'"

        area = 330

        blub = self.query_return(conn, sel, fro, whe)
        list = self.show_next(blub, area)
        return list

    def getUnsortedList(self):
        conn = self.create_connection("../pcdrdata.sqlite3")

        sel = "IDNumber, DeviceDescription, NextTest"
        fro = "tblIDNumbers"
        whe = "TestResult = 'OK'"

        return self.query_return(conn, sel, fro, whe)
