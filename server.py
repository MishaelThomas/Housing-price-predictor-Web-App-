#pip install flask
#pip install request

from flask import Flask, jsonify, request
import util

app = Flask(__name__)

@app.route('/get_column_names',methods=['GET'])
def get_column_names():
    response = jsonify({'Columns' : util.get_data_columns()})
    return response

@app.route('/predict_housing_price',methods=['POST'])
def predict_housing_price():
    area_type = request.form['area_type']
    availability = request.form['availability']
    location = request.form['location']
    size = request.form['size']
    society = request.form['society']
    sqft = float(request.form['sqft'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])

    response = jsonify({'predicted_price': util.predict_price(area_type,availability,location,size,society,sqft,bath,balcony)[0]})

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

util.load_artifacts

app.run()
