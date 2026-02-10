from flask import Flask,request,jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names',methods = ['GET'])
def get_location_name():
    response = jsonify({
        'location':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/home_price',methods = ['GET','POST'])
def home_price():
    location = request.form.get('location')
    sqft = float(request.form.get('sqft',0))
    bhk = int(request.form.get('bhk',0))
    bath = int(request.form.get('bath',0))

    response2 = jsonify({
        'estimated_predict': util.model_predict(location,sqft,bhk,bath)
    })
    response2.headers.add('Access-Control-Allow-Origin', '*')
    return response2



if __name__ == '__main__':
    print("string for home prediction")
    util.get_artifact_names()
    app.run()