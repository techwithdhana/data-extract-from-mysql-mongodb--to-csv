import pymongo
from pymongo import MongoClient

# integrate with mongodb
connect = MongoClient('localhost', 27017) # database details
dbName = connect.college # connect to the database

tableName = dbName.students # navigate the table/collection
studentList = tableName.find() # retrive the details from table

# for records in studentList:
# 	print(records)

import pandas as pd

df = pd.DataFrame(list(studentList)) # convert the data frame format
df.to_csv('mongodb.csv') # save as csv file
print("file saved")
print(df)
