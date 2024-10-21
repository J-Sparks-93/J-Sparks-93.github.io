#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hardwired to use the aac database, the animals collection, and the aacuser.
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

    #This method is used to create documents for the database.
    
    #So far I have updated the naming conventions to better suit what the functions of the variables. - Jeffrey Sparks
    
    def create(self, createData):
        if document is not None:
            insert = self.database.animals.insert_one(createData)
            if insert != 0:
                return True
                print('True')
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    #This method is used to read documents from the database
    def read(self, readData):
        if readData is not None:
            return self.database.animals.find(readData)
        else:
            raise Exception("Nothing to read, because data parameter is empty")

    #This function sets up "GetRecords" which pulls multipole documents instead of a single document
    #Get records with criteria(Keywords for query search)
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
        
    #This method creates the update function, updating the data within the database.
    def update(self, initialData, updatedData):
        if initialData is not None:
            if self.database.animals.count_documents(initialData, limit = 1) != 0:
                update_result = self.database.animals.update_many(initialData,{"$set":updatedData})
                result = update_result.raw_result
                return result
                
        else:
            raise Exception("Nothing to update, because data parameter is empty")

   
            
    #This method implements the delete function, this allows you to delete documents from the database
    def delete(self, deletedData):
        if deletedData is not None:
            if self.database.animals.count_documents(deletedData, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(deletedData)
                result = delete_result.raw_result
                return result
            
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

