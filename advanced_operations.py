########## Working with Embeded Documents ########## 
import pymongo
import pymongo.errors
import json


class embeded(object):

    def connection(self):

        """
        Creating a connection.
        """

        try:
            c = pymongo.Connection(host="127.0.0.1", port=27017)
        except pymongo.errors.ConnectionFailure, e:
            raise "Could not connect to database."

        return c

    def insert_document(self, c):

        """
        Inserting a embeded Document in to database.
        """

        # Creating a database handler
        dbh = c["person_db"]

        data = {"username":"Prabhath",
                "emails":[
                   {
                       "email":"prabhath@hotmail.com",
                       "primary":True
                       },
                   {
                       "email":"prabhath@gmail.com",
                       "primary":False
                       },
                   {
                       "email":"prabhath@yahoo.com",
                       "primary":True
                       }
                   ]
                }

        # Inserting into db
        dbh.embeded.insert((data), safe=True)

        print "Done Inserting"

    def query1(self, c):

        """
        Searching for only primary emails.
        """

        # Handler
        dbh = c["person_db"]

        # Primary emails
        data = dbh.embeded.find({"username":"Prabhath"})

        for i in list(data):
            for k in i["emails"]:
                if k["primary"]==True:
                    print k


    def query2(self, c):

        """
        Updating email
        """

        # Handler
        dbh = c["person_db"]

        # Update hotmail
        data = dbh.embeded.update(
                {"emails.email":"prabhath@hotmail.com"},
                {"$set":{"emails.$.email":"prabhath6@hotmail.com"}}, safe=True)
        
        data1 = dbh.embeded.find({"username":"Prabhath"})

        for i in list(data1):
            for k in i["emails"]:
                print k

    def query3(self, c):

        """
        Removing one element from embeded query.
        """

        # Handler
        dbh = c["person_db"]

        # Remove yahoo
        data = dbh.embeded.update({"username":"Prabhath"},
                {"$pull":{"emails": {"email":"prabhath@yahoo.com"}}},
                safe=True)


        data1 = dbh.embeded.find({"username":"Prabhath"})

        for i in list(data1):
            for k in i["emails"]:
                print "Update document:",  k


    def query4(self, c):

        """
        Adding one element to embeded query.
        """

        # Handler
        dbh = c["person_db"]

        # Remove yahoo
        data = dbh.embeded.update({"username":"Prabhath"},
                {"$push":{"emails": {"email":"prabhath@yahoo.com",
                    "primary":False}}},safe=True)


        data1 = dbh.embeded.find({"username":"Prabhath"})

        for i in list(data1):
            for k in i["emails"]:
                print "Update document2:",  k


if __name__ == "__main__":
    p = embeded()

    # Creating a connection
    c = p.connection()
    # Inserting into schema
    p.insert_document(c)

    p.query1(c)
    p.query2(c)
    p.query3(c)
    p.query4(c)
