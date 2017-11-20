import csv
import requests
from flask import Flask


app = Flask(__name__)

@app.route('/')
def display():
	chuck_call(10)


def chuck_call(n):
	url = 'http://api.icndb.com/jokes/random/'
	for i in range(n):
		response = requests.get(url)
		html = response.content
		store_joke_internally(html)

def store_joke_internally(joke):
	with open('./jokes_storage.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([joke])


if __name__ == '__main__':
	app.run(debug=True)

