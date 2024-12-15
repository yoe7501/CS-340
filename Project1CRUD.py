from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        # Connection variables for the MongoDB database
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31907
        DB = 'AAC'
        COL = 'animals'

        # Initialize the MongoClient with error handling
        try:
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("Successfully connected to MongoDB.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    def create(self, data):
        """Insert a document into the MongoDB collection."""
        if data and isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error inserting data: {e}")
                return False
        else:
            raise ValueError("Invalid data: Must provide a non-empty dictionary.")

    def read(self, query=None):
        """Query documents from the MongoDB collection."""
        try:
            data = list(self.collection.find(query or {}))
            if not data:
                print("No records found for the given query.")
            return data
        except Exception as e:
            print(f"Error querying data: {e}")
            return []

    def update(self, query, new_values):
        """Update document(s) in the MongoDB collection."""
        if query and new_values and isinstance(query, dict) and isinstance(new_values, dict):
            try:
                result = self.collection.update_many(query, {'$set': new_values})
                return result.modified_count
            except Exception as e:
                print(f"Error updating data: {e}")
                return 0
        else:
            raise ValueError("Invalid query or new values: Must provide non-empty dictionaries.")

    def delete(self, query):
        """Delete document(s) from the MongoDB collection."""
        if query and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting data: {e}")
                return 0
        else:
            raise ValueError("Invalid query: Must provide a non-empty dictionary.")

