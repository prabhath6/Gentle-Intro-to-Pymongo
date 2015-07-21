__author__ = 'prabhath'

import pymongo
import pymongo.errors
import json
from datetime import datetime

""" In this i will be using a versatile database """

class insert_into_db(object):

    def connection(self):

        try:
            c = pymongo.Connection(host="127.0.0.1", port = 27017)
        except pymongo.errors.ConnectionFailure, e:
            raise "COuld not establish connection with db"

        return c

    def insert_data(self, c):

        """
        Some versatile db rows
        """

        data1 ={"name":"Prabhath", "dob":datetime(2013, 1, 1), 'weight':120, "loves": ["carrot", "mango"], "gender":"m"} 
        data2 ={"name":"Rahul", "dob":datetime(2013, 2, 1), 'weight':125, "loves": ["banana", "grapes"], "gender":"m"} 
        data3 ={"name":"Kiran", "dob":datetime(2013, 3, 1), 'weight':126, "loves": ["oranges", "banana"], "gender":"m"}
        data4 ={"name":"Srinivas", "dob":datetime(2013, 4, 1), 'weight':128, "loves": ["tacobel", "banana"], "gender":"m"}
        data5 ={"name":"rani", "dob":datetime(2013, 5, 1), 'weight':138, "loves": ["tacobel", "subway"], "gender":"f"}
        data6 ={"name":"venus", "dob":datetime(2013, 4, 29), 'weight':108, "loves": ["chicken", "sweets"], "gender":"f"}

        data = [data1, data2, data3, data4, data5, data6]

        # dbh handler
        dbh = c["person_db"]

        "Insert data into versatile schema"

        for i in data:
            dbh.versatile_db.insert(i, safe=True)

        print "Done Inserting data."

if __name__ == "__main__":

    p = insert_into_db()
    r = p.connection()

    # Insert data
    p.insert_data(r)
