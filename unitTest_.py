import os
import unittest
from ghapi.all import GhApi
import utils_.utils_ as utils

create_table = 'CREATE TABLE githubUsers (\
		idx	INTEGER PRIMARY KEY,\
		Username	TEXT,\
		githubId	INTEGER,\
		imageUrl	TEXT,\
		userType	TEXT,\
		linkToGitHub	TEXT\
		)'



class TestStringMethods(unittest.TestCase):
	def test_connect_to_unexistent_db( self ):
		#delete the file in case that exists
		try:
			os.remove('unit_test_db.db')
		except:
			print( "File doesn\'t exists" )

		database = utils.my_sql_class('unit_test_db.db')

		#if database is empty, then the number of tables is 0
		database.cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table';")

		self.assertEqual(0,len(database.cursorObj.fetchall()))

		database = None

		os.remove('unit_test_db.db')

	def test_add_table_githubUsers(self):

		try:
			os.remove('unit_test_db.db')
		except:
			print( "File doesn\'t exists" )

		database = utils.my_sql_class('unit_test_db.db')

		database.execute_query( create_table )

		database.cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table';")

		self.assertEqual(1,len(database.cursorObj.fetchall()))

		database = None

		os.remove('unit_test_db.db')


	def test_add_row_to_githubUsers(self):

		try:
			os.remove('unit_test_db.db')
		except:
			print( "File doesn\'t exists" )

		database = utils.my_sql_class('unit_test_db.db')

		database.execute_query( create_table )

		database.add_row( 0, [1,'2',3,'4','5','6'] )

		database.cursorObj.execute("SELECT * FROM githubUsers;")
		
		results = database.cursorObj.fetchall()

		database = None

		os.remove('unit_test_db.db')

		self.assertEqual( (0, '1', 2, '3', '4', '5'), results[0] )
		self.assertEqual( 1, len(results) )

	
	def test_len_of_results( self ):
		
		api = GhApi()
		self.assertEqual( 15, len( utils.search_users(api,'tom', 15) )  )
		self.assertEqual( 100, len( utils.search_users(api,'tom', 100) )  )

		#Since the max number is 100 for unregistered users
		self.assertEqual( 100, len( utils.search_users(api,'tom', 1000) )  )



"""
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""
if __name__ == '__main__':
    unittest.main()


	

