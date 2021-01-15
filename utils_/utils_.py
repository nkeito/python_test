from ghapi.all import GhApi
import sqlite3
from sqlite3 import Error

#A wrapper for sqlite 
class my_sql_class():
	def __init__(self, databaseName):
		self.name = databaseName
		try:
			self.con = sqlite3.connect(databaseName)
			self.cursorObj = self.con.cursor()
		except Error:
			print(Error)

	#Executes a query in the database
	def execute_query(self, query):
		try:
			self.cursorObj.execute(query)
			self.con.commit()
			return True
		except Error:
			print('Cannot execute query: {0}'.format(query))
			return False

	#Adds a row to the given table
	def add_row( self, idx,row ):
		q = "INSERT INTO githubUsers VALUES({0}, \'{1}\', {2}, \'{3}\', \'{4}\', \'{5}\' )".format( idx ,row[0],row[1],row[2],row[3], row[4]  )
		self.execute_query(q)


		

# Search users based on his name, #repos and followers
def search_users(api, name, total=150 ):
	results = api.search.users(name,'repos', 'followers',str(total)) 
	return [ [item['login'], item['id'], item['avatar_url'] , item['type'] , item['html_url'] ] for item in  results['items'] ]

	

