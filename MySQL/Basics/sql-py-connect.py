


import mysql.connector as sql
import pandas as pd


connect = sql.connect(
	host = 'localhost',
	user = 'root',
	password = '1994',
	database = 'office')

print(connect)

df = pd.read_sql('select * from employeedetails', con = connect)
print(df.head())
df.to_csv('empDetails.csv')
print('Data Saved')

