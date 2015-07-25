############### Queries ###############

import pymongo
import pymongo.errors


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
    
    def query2(self, c):

        # Create a database handler
        dbh = c["person_db"]

        """
        Returns any person who loves oranges or sweets
        """

        data = dbh.versatile_db.find({"loves":{"$in":["sweets", "oranges"]}})
    
        for i in data:
           print i 

    def query3(self, c):

        # Create a database handler
        dbh = c["person_db"]

        """
        Using 'or' 
        """
        
        data = dbh.versatile_db.find({"gender": "f", 
            "$or":[{"loves":"sweets"},{"weight":138}]})
        
        for i in data:
            print i
    
    def query4(self, c):

        # Create a database handler
        dbh = c["person_db"]
        
        """
        Using 'push' to append
        """

        data = dbh.versatile_db.update({"name":"Prabhath"},
                {"$push": {"loves": "sugar"}})

        data1 = dbh.versatile_db.find({"name":"Prabhath"})

        for i in data1:
            print i
        
        # Removing sugar
        dbh.versatile_db.update({"name":"Prabhath"}, 
                {"$pull":{"loves":"sugar"}})

if __name__ == "__main__":

    p = query()
    c = p.connection()
    # q1
    p.query1(c)
    print 
    # q2
    p.query2(c)
    print 
    # q3
    p.query3(c)
    # q4
    print
    p.query4(c)
