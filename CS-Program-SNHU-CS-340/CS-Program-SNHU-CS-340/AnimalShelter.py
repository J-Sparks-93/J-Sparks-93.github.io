#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hardwired to use the aac database, the andimals collection, and the aacuser.
        # Definitions of the connection string variables are unique to the individual Apporto environments. 
        # you must edit the connection variables below to reflect your own instance of MongoDB!
        
        #Connection Variables
        
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30645
        DB = 'AAC'
        COL = 'animals'
        #
        #Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database ['%s' % (COL)]
        
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)
            if insert != 0:
                return True
                print('True')
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    #Implement read method
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data)
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            
     #Get records with criteria
    #All records are returned if criteria is None
    #Default is None
    #Example: ({""name": "Rex", 'age_upon_outcome': '2 months'})
    #do not return the _id
    def getRecordCriteria(self, criteria):
        if criteria:
            _data = self.database.animals.find(criteria, {'_id' : 0})
                                 
        else:
            _data = self.database.animals.find({},{'_id' : 0})
                                  
        return _data
    #Implement update method
    def update(self, initial, data):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial,{"$set":data})
                result = update_result.raw_result
                return result
                
        else:
            raise Exception("Nothing to update, because data parameter is empty")
    #Implement delete method
    def delete(self, data):
        if data is not None:
            if self.database.animals.count_documents(data, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(data)
                result = delete_result.raw_result
                return result
            
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

