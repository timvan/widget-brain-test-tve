import csv
import requests
from flask import Flask


app = Flask(__name__)

@app.route('/')
def display():
	init_db()
	get_joke(10)
	return "Hi, welcome to Chuck Norris joke machine"

@app.route('/getJokes')
def return_jokes():
	"""read database for all jokes
	return page with jokes seperated by html linespace
	"""
	page = ""
	with open('./jokes_storage.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			print (row[1])
			page += ((row)[1] + "<br />")
	return (page)


@app.route('/flushJokes')
def flush_jokes():
	"""Remove database entries by re-intialising the database
	"""
	init_db()
	return "Flushed jokes: re-intiailised database"

@app.route('/getNewJokes')
def getNewJokes():
	get_joke(10)
	return "getting jokes"


def chuck_call(n):
	"""Call for Chuck Norris n jokes
	Return dictionary of Chuck Norris values
	"""
	print ("chuck_call")
	url = 'http://api.icndb.com/jokes/random/' + str(n)
	response = requests.get(url)
	data = response.json()
	return data


def get_joke(n):
	"""Write to jokes_storage.csv
	Initialise the databse
	Call for Chuck Norris jokes n times and append to ./jokes_storage.csv
	"""
	print ("get_joke")
	data = chuck_call(n)
	with open('./jokes_storage.csv', 'a') as f:
		writer = csv.writer(f)
		for i in range(n):
			writer.writerow([data['value'][i]['id'], data['value'][i]['joke'],
			 	data['value'][i]['categories']])


def init_db():
	"""Intialise the database with heading
	"""
	print ("init_db")
	headings = ['id', 'joke', 'categories']
	with open('./jokes_storage.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(headings)
	return

if __name__ == '__main__':
	app.run(debug=True)

"""
TODO:

- Check if call is succesfuly or not, only store if succes
- for chuck_call - check / wait for a response
- init_db should first check if exists, 
- flushJokes - should delete database rows instead of re-initialising
- build html & css front


"""