# python_test
Python test for github API and Display results in Flask

Prerrequisites:
GHApi as interface for github API
Flask to display the results
flask_sqlalchemy for reading the database from step 1.

pip3 install ghapi Flask flask_sqlalchemy

Execution

$bash execute_production.sh

The script execute_production.sh will query the first 150 records (100 actually due to the lack of token) of github users by popularity i.e.
number of repos and followers, who match the criteria of username provided in said file. After that, it will initialize a flask app which shows the results of the query,
paginated every 25 records.

Explanaiton
In order to keep everything as pythonic as possible, I deceided to use the ghapi library to query from github api, as there wasn't any requisite for the query other than the lenght, I choose to follow the example displayed in the documentation, and then I encapsulated it into the function 'search_users' which takes the username and the max number of results to be obtained as parameters.
After that, I deceided to assume that the table 'mydatabase.db' existed (which is not allways the case, as the unit test show). Then, using a wrapper class for sqlite3 I was able to store the results as rows of the table githubUsers.
Finally, in order to display the query results, I modified this tutorial https://medium.com/better-programming/simple-flask-pagination-example-4190b12c2e2e for the required purposes. The actual webpage is located in the folder flask_webpage.

