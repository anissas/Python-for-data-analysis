from flask import Flask, jsonify
import joblib
from joblib import dump, load
import traceback
import sys
from flask import request
import pandas as pd



app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['POST'])
def predict():
    if Dtree:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(Dtree.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


if __name__ == '__main__':
    Dtree = joblib.load('model.pkl')
    print ('Model loaded')
    model_columns = joblib.load('model_columns.pkl') # Load "model_columns.pkl"
    print ('Model columns loaded')
    app.run(debug=True, port=80)