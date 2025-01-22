from flask import Flask, jsonify, request
import random
import threading
import time
from sklearn.datasets import load_breast_cancer
import pickle
import pandas as pd

app = Flask(__name__)

current_data = pd.read_csv('test_data.csv')
print(len(current_data))

with open('best_rf.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/datos', methods=['GET'])
def get_data():
    row = current_data.iloc[0]
    dato = row.to_dict()
    dato['id'] = current_data.index[0]  # Asignar el índice como 'id'
    current_data.drop(current_data.index[0], inplace=True)
    return jsonify(dato)

@app.route('/predict', methods=['POST'])
def predecir():
    data = request.get_json()
    input_modelo = [list(data.values())]
    prediccion = model.predict(input_modelo)[0]

    return jsonify({'prediccion': prediccion})

if __name__ == '__main__':
    # Ajusta host/puerto según tus necesidades
    app.run(debug=True, host='0.0.0.0', port=5000)
