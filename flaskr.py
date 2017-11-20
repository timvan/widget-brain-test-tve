import csv
import requests
from flask import Flask


app = Flask(__name__)

@app.route('/')
def display():
	return "Hi, welcome to Chuck Norris joke machine"
	get_joke(10)

@app.route('/getJokes')
def return_jokes():
	page = ""
	with open('./jokes_storage.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			print (row[1])
			page += ((row)[1] + "<br />")
	return (page)

def chuck_call():
	"""Call for Chuck Norris jokes
	Return dictionary of Chuck Norris values
	"""
	url = 'http://api.icndb.com/jokes/random/'
	response = requests.get(url)
	data = response.json()
	return data

def get_joke(n):
	"""Write to jokes_storage.csv
	First erase and write headings to jokes_storage.csv
	Second call for Chuck Norris jokes n times and append to ./jokes_storage.csv
	"""
	headings = ['id', 'joke', 'categories']
	with open('./jokes_storage.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(headings)

	with open('./jokes_storage.csv', 'a') as f:
		writer = csv.writer(f)
		for i in range(n):
			data = chuck_call()
			writer.writerow([data['value']['id'], data['value']['joke'],
			 	data['value']['categories']])

if __name__ == '__main__':
	app.run(debug=True)

"""
TODO:

- Check is call is succesfuly or not, only store if succes

"""