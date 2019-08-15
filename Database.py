import pymongo
from bson import ObjectId

connection = pymongo.MongoClient("localhost", 27017)

database = connection["mydb_01"]

collection = database['mycol_01']
print("Database connected.")


def insert_data(data):
	"""
	Insert new data or document in collection
	:param data
	:return
	"""
	document = collection.insert_one(data)
	return document.inserted_id

def update_or_create(document_id, data):
	"""
	This will create a new document in the collection
	If same document ID exists then update data
	:param document_id
	:param data
	:return
	"""
	document = collection.update_one({'_id':OjectId(document_id)}, {'$set':data}, upsert=True)
	return document.acknowledged
	
def get_single_data(document_id):
	"""
	get document data by document ID
	:param document id
	:return
	"""
	
	data = collection.find_one({'_id':ObjectID(document_id)})
	return data
	
def get_multiple_data():
	"""
	get document data by document ID
	:return
	"""
	
	data = collection.find()
	return list(data)
	
def update_existing(document_id, data):
	return document.acknowledged
	
def remove_data(document_id):
	document = collection.delete_one({'_id':ObjectId(document_id)})
	return document.acknowledged
	
#CLOSE DATABASE
connection.close()




