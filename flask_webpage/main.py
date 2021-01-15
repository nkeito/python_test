from flask import Flask, render_template, request
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pathlib

#read db path
dbPath = pathlib.Path(__file__).parent.absolute()
dbPath = "/".join( x for x in str(dbPath).split("/")[:-1] ) + '/mydatabase.db'    



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbPath
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


#Convert the sqlite table to something that we can understand
class User(db.Model):
	__tablename__ = 'githubUsers'
	__table_args__ = { 'extend_existing': True }
	idx = db.Column(db.Integer, primary_key=True)


#render index webpage
@app.route('/')
def index():
    return render_template('index.html')

#Display the content of the database
ROWS_PER_PAGE = 25
@app.route('/GhUsers')
def GhUsers():
    # Set the pagination configuration
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template('GhUsers/all_users.html', colors=users)
