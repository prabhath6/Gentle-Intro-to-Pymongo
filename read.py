########## Reading from the data base ########## 
import pymongo
import pymongo.errors


class read_db(object):

    def connection(self):

        """
        Creating a connection Object
        """

        try:
            c = pymongo.Connection(host = "127.0.0.1", port = 27017)
        except pymongo.errors.ConnectionFailure, e:
            raise "Could not connect to data base"

        return c
    
    def query(self, c):

        """
        Querying the data base.
        """

        # Create a data base handler
        dbh = c["person_db"]

        # my name
        data = dbh.users.find({"fname":"Prabhath"})

        for i in data:
            print "Age : {}" .format(i["age"])
    
    def query1(self, c):


        # Create a data base handler
        dbh = c["person_db"]

        # Age
        data = dbh.users.find({"degree":"masters"}, {"age" : 1})

        for i in  data:
            print "Age : {}" .format(i.get('age'))
    
    def query2(self, c):

        """
        Total number of people with age 24.
        """

        # Create a data base handler
        dbh = c["person_db"]

        # Getting Count
        data = dbh.users.find({"age" : 24}).count()

        print "Total number of people with age 24 are {}" .format(data)

    def query3(self, c):

        """
        Total number of peolpe with age greater than 23.
        """

        # Create a data base handler
        dbh = c["person_db"]

        # Count of people with age greater than 23
        data = dbh.users.find({"age":{"$gt":23}}).count()

        print "Total number of people with age greater than 23 are {}." .format(data)


    def query4(self, c):
        
        """
        Sorting
        """

        # Create a data base handler
        dbh = c["person_db"]

        # Sorting based on id
        data = dbh.users.find({"degree":"masters"}, sort=[("id", pymongo.DESCENDING)])

        for i in  data:
            print "Firstname: {}, Age : {}" .format(i.get("fname"), i.get('age'))

    def query5(self, c):

        """
        Updating database.
        """
        # Create a data base handler
        dbh = c["person_db"]

        # Updating the database
        dbh.users.update({"fname":"kiran"},
                {"$set":{"degree":"PHD"}}, safe=True)
        
        data = dbh.users.find_one({"fname": "kiran"})

        print "Name: {}, age: {}, degree: {}" .format(data['fname'], 
                data['age'], data['degree'])

    def query6(self, c):

        """
        Deleting a Document in collection.
        """
        # Create a data base handler
        dbh = c["person_db"]

        # deleting a dummy collection
        dbh.users.insert({"id":10, "fname":"a","lname":"b", "age":25, "degree":"ms"})

        data = dbh.users.find_one({"fname":"a"})
        print data['fname']

        dbh.users.remove({"fname":"a"}, safe=True)

        data1 =  dbh.users.find_one({"fname":"a"})
        print data1

if __name__ == "__main__":
   p = read_db()
   r = p.connection()

   # Normal query to get age.
   p.query(r)

   # To get all the people's age who's degree is masters.
   p.query1(r)

   # To get number of people with age equals 24
   p.query2(r)

   # To get count of people with age greater than 23
   p.query3(r)

   # Sorting
   p.query4(r)

   # Updating
   p.query5(r)

   # Delting a document
   p.query6(r)
