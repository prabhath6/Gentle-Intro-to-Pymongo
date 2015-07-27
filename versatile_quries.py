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

    def query5(self, c):

        # Create a database handler
        dbh = c["person_db"]

        """
        Updating all the documents in the data base.
        """

        dbh.versatile_db.update({},{"$set": {"vaccinated":True}}, multi= True)

        data = dbh.versatile_db.find({"vaccinated":True})

        for i in data:
            print i["name"]

    def query6(self, c):

        # Create a database handler
        dbh = c["person_db"]

        """
        Removing vaccinated field from all the documents in the data base.
        """
        dbh.versatile_db.update({}, {"$unset":{"vaccinated":""}}, multi= True)
        
        """
        Modifing a single document

        dbh.versatile_db.update({"name":"Rahul"}
            ,{"$unset":{"vaccinated":""}})
        """

        data = dbh.versatile_db.find({})

        for i in data:
            print i
    
    def query7(self, c):

        # Create data base handler
        dbh = c["person_db"]

        """
        Custom selection of fileds in a document.
        By default every time _id is returned when
        find is used we can exclude it using.
        """
        data = dbh.versatile_db.find({},{"name": 1, "weight": 1, "_id": 0})

        for i in data:
            print i
    
    def query8(self, c):

        # Create a databse handler
        dbh = c["person_db"]

        """
        Odering 
        Sorting can be done in two ways
        1. dbh.person_db.find({}, sort=[(field_name, order)])
        2. dbh.person_db.find({}).sort([(field_name: -1)])
        -1 = descending order
         1 = ascending order
        """

        data = dbh.versatile_db.find({}).sort([("weight", -1)])

        for i in data:
            print i['weight']

    def query9(self, c):

        # Create a database handler
        dbh = c["person_db"]

        """
        Using limit and skip.
        limit is used to limit the number of values in the result set
        skip is used to skip the elemet in the result set.(2nd highest)
        """
        data = dbh.versatile_db.find({}).sort([("weight", -1)]).limit(3).skip(1)

        for i in data:
            print i['weight']
           

    def query10(self, c):

        # Create a database handler
        dbh = c["person_db"]

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
    print 
    p.query5(c)
    print 
    p.query6(c)
    #print 
    #p.query7(c)
    #print 
    #p.query8(c)
    print
    p.query9(c)
