############### Queries ###############

import pymongo
import pymongo.errors
import json

class query(object):
    
    def connection(self):

        try:
            c = pymongo.Connection(host="127.0.0.1", port=27017)
        except pymongo.errors.ConnectionFailure, e:
            raise "Cannot connect to database"
        
        return c

    def query1(self, c):

        # Create database handler
        dbh = c["person_db"]

        data = dbh.versatile_db.find({"gender": {"$ne":"f"},"weight":{"$gte":125}})

        for i in data:
            print i

if __name__ == "__main__":

    p = query()
    c = p.connection()
    p.query1(c)
