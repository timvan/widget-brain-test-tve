import csv
import urllib2

from flask import Flask

app = Flask(__name__)

@app.route('/')
def display():
	return "it works!"

if __name__ == '__main__':
	app.run(debug=True)

