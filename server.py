
# Create a rest api server using flask

from flask import Flask, jsonify, request 
from flask_restful import Resource, Api, abort

app = Flask(__name__) 
api = Api(app) 

# import data from csv file
import csv

# read a csv file
with open('CrimeMusicData.csv', 'r') as file:
		reader = csv.reader(file)
		data = list(reader)


header = ['ID','Country','Year','Index','Rank','Crime Rate','Hip hop/Rap/R&b','EDM','Pop','Rock/Metal','Latin/Reggaeton','Other','Average_Day_Length']
class Country(Resource): 
	def get(self, country):
		res = []
		for i in range(len(data)):
			if data[i][1].lower() == country.lower():
				res.append(data[i])
		if len(res) > 1:
			return jsonify({'data': 		
									list(map(lambda x: 
									dict(zip(header, x)), res))
			})
		elif len(res) == 1:
			return jsonify({'data': dict(zip(header, res[0]))})
		else:
			# return status code 404
			abort(404, message="No data found for this country")

api.add_resource(Country, '/country/<string:country>')




if __name__ == '__main__': 
	app.run(debug = True) 



# 