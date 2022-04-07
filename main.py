import pymongo

# connecting
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# seeing how many database we  have
collist = myclient.list_database_names()
# print(collist,"databases")

#creationg database name
mydb = myclient["mydatabase"]

# creating collection
mycol = mydb['Customer']

#  creating collection
# mydict = [{ "name": "John", "address": "Mumbai" },
#           { "name": "Rema", "address": "Surat" },
#           { "name": "Megha", "address": "Delhi" },
#           { "name": "Bharti", "address": "Bihar" },
#           { "name": "Raghav", "address": "Rajori" }]


# # inserting more thanone  data 
# x = mycol.insert_many(mydict)

# # inserting one  data 
# mydict = { "name": "John", "address": "Mumbai" },
# x = mycol.insert_one(mydict)

# checking if collection is exists in  my database
if 'mydatabase' in collist:
  print("The collection exists.")
else:
    print("The collection doesn't exists")


# # find_one use to show one  data
# x = mycol.find_one()
# print(x)

# # find use to show all the data
# x = mycol.find()
# for i in x:
#     print(i)

# 0 = not visible, 1 = is viisble
# a = mycol.find({},{ "_id": 0, "name": 1})
# for x in a :
#     # for values
# #   print(x['name'])
#   print(x)
  
  
# filtering the condition using find
# myquery = {"name":"Megha"}
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)
  
# filtering the data ^M means starting with M
# myquery = {"name":{"$regex":"^M"}}
# mydoc = mycol.find(myquery)

# for x in mydoc:
#   print(x)
  
  
# sorting data 
# sort("name", 1) #ascending
# sort("name", -1) #descending
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#   print(x)

# first priority wo first sort ko dega
# mydoc = mycol.find().sort("name").sort('address')
# for x in mydoc:
#   print(x)


# delete one
# myquery = { "address": "Delhi" }
# mycol.delete_one(myquery)

# delete many
# x = mycol.delete_many({'name':'John'})
# print(x.deleted_count, " documents deleted.")

# drop the  collection
# mycol.drop()


# update one
# myquery = { "address": "Bihar" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)

#print "customers" after the update:
# for x in mycol.find():
#   print(x)


# update many
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

# limit
# myresult = mycol.find().limit(5)
# #print the result:
# for x in myresult:
#   print(x)