import sys
from ghapi.all import GhApi
import utils_.utils_ as utils 



if __name__ == '__main__':

	userName = ""

	if len(sys.argv) == 1:
		userName = 'tom'
	else:
		userName = sys.argv[1]

	#fetch data using ghapi
	api = GhApi()
	results = utils.search_users(api,userName, 150)

	#Connect to database
	database = utils.my_sql_class('mydatabase.db')

	create_table = 'CREATE TABLE githubUsers (\
	idx	INTEGER PRIMARY KEY,\
	Username	TEXT,\
	githubId	INTEGER,\
	imageUrl	TEXT,\
	userType	TEXT,\
	linkToGitHub	TEXT\
	)'
	

	if database.execute_query( create_table ) == False:
		database.execute_query( 'DROP TABLE githubUsers' )
		database.execute_query( create_table )


	for k, item in enumerate(results):
		database.add_row(  k,item  )


	

