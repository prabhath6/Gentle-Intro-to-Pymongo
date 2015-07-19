import pymongo
import pymongo.errors
import json

def connection():

    """
    Creating a connection object to the mongodb database.
    """

    try:
        c = pymongo.Connection(host="127.0.0.1", port=27017)
    except pymongo.errors.ConnectionFailure, e:
        raise "Could not connect to the pymongo database."

    return c

def reading_data(fileName):

    '''
    Reading rows from the file created.
    '''

    with open(fileName,'r') as data:
        return data.readlines()

def inserting_data_into_db(c, data):

    '''
    Inserting data into db that is read from the
    file provided which contains rows.
    '''

    # Getting a database handler
    dbh = c["person_db"]

    # Inserting data
    final = [ ]

    for i in data:
        final.append(json.loads(i))

    dbh.users.insert(final, safe = True)

    print "Done inserting."

if __name__ == "__main__":
    inserting_data_into_db(connection(), reading_data("data.txt"))
