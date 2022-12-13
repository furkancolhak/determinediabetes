import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__)

model2 = keras.models.load_model('C:/Users/enes/Desktop/cloudproject/model.h5')

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('index.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction[prediction <= 0.5] = 0.
    prediction[prediction > 0.5] = 1.
    if prediction[0] == 1:
        a ="Diabetes"
    else:
        a="Not Diabetes"
    

    
    return render_template('index.html', prediction_text="Checking Diabetes: {}".format(a))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True)