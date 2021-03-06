from flask import Flask, request, jsonify, render_template
import util
import os

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return render_template('app.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    hst = '127.0.0.1'
    prt = 5000
    if 'PORT' in os.environ:
        hst = '0.0.0.0'
        prt = os.environ['PORT']
    app.run(host=hst, port=int(prt))
