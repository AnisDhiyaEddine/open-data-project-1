
# Create a rest api server using flask

from flask import Flask, jsonify, request 
from flask_restful import Resource, Api, abort

app = Flask(__name__) 
api = Api(app) 

# import data from csv file
import csv

# read a csv file
with open('data.csv', 'r') as file:
		reader = csv.reader(file)
		data = list(reader)

 
class Country(Resource): 
	def get(self, country):
		res = []
		for i in range(len(data)):
			if data[i][1] == country:
				res.append(data[i])
		if len(res) > 1:
			return jsonify({'data': 		
									list(map(lambda x: {
										'country': x[1],
										'year': x[2],
										'music_type': x[3],
										'happiness_score': x[4],
										'happiness_rank': x[5],
										'daylight_duration': x[6],
										'crime_rate': x[7]
									}, res))
			})
		elif len(res) == 1:
			return jsonify({'data': {
				'country': res[0][1],
				'year': res[0][2],
				'music_type': res[0][3],
				'happiness_score': res[0][4],
				'happiness_rank': res[0][5],
				'daylight_duration': res[0][6],
				'crime_rate': res[0][7]
			}})
		else:
			# return status code 404
			abort(404, message="No data found for this country")

api.add_resource(Country, '/country/<string:country>')




if __name__ == '__main__': 
	app.run(debug = True) 



# 