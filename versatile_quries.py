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
