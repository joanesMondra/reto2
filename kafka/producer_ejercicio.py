import json
import requests
from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print(f"Error enviando mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

producer = Producer({'bootstrap.servers': 'localhost:9092'})

# URL del servicio Flask
url_datos = 'http://127.0.0.1:5000/datos'
url_prediccion = 'http://127.0.0.1:5000/predict'

while True:
    response = requests.get(url_datos)
    if response.status_code == 200:
        datos = response.json()

        # Construimos el diccionario de features con las claves exactas que mencionaste
        features = {
            "microphone_median": datos["microphone_median"],
            "microphone_dominant_frequency": datos["microphone_dominant_frequency"],
            "acc_under_radiale_dominant_frequency": datos["acc_under_radiale_dominant_frequency"],
            "acc_under_tangencial_kurtosis": datos["acc_under_tangencial_kurtosis"],
            "acc_under_tangencial_mean": datos["acc_under_tangencial_mean"],
            "acc_under_axial_range": datos["acc_under_axial_range"],
            "acc_over_axial_std": datos["acc_over_axial_std"],
            "acc_over_radiale_range": datos["acc_over_radiale_range"],
            "acc_over_axial_range": datos["acc_over_axial_range"],
            "acc_over_axial_variance": datos["acc_over_axial_variance"],
            "microphone_mean": datos["microphone_mean"],
            "acc_over_radiale_std": datos["acc_over_radiale_std"],
            "acc_under_axial_std": datos["acc_under_axial_std"],
            "microphone_kurtosis": datos["microphone_kurtosis"],
            "acc_under_axial_variance": datos["acc_under_axial_variance"],
            "acc_over_radiale_variance": datos["acc_over_radiale_variance"],
            "acc_under_radiale_skewness": datos["acc_under_radiale_skewness"],
            "acc_over_tangencial_dominant_frequency": datos["acc_over_tangencial_dominant_frequency"],
            "acc_over_tangencial_std": datos["acc_over_tangencial_std"],
            "acc_over_tangencial_variance": datos["acc_over_tangencial_variance"],
            "acc_over_radiale_skewness": datos["acc_over_radiale_skewness"],
            "acc_under_axial_dominant_frequency": datos["acc_under_axial_dominant_frequency"],
            "acc_under_radiale_kurtosis": datos["acc_under_radiale_kurtosis"],
            "microphone_skewness": datos["microphone_skewness"],
            "microphone_range": datos["microphone_range"],
            "acc_over_tangencial_range": datos["acc_over_tangencial_range"],
            "acc_over_radiale_kurtosis": datos["acc_over_radiale_kurtosis"],
            "acc_under_radiale_variance": datos["acc_under_radiale_variance"],
            "acc_under_tangencial_skewness": datos["acc_under_tangencial_skewness"],
            "acc_under_radiale_std": datos["acc_under_radiale_std"],
            "acc_under_tangencial_dominant_frequency": datos["acc_under_tangencial_dominant_frequency"],
            "acc_under_radiale_median": datos["acc_under_radiale_median"],
            "acc_under_tangencial_median": datos["acc_under_tangencial_median"],
            "microphone_std": datos["microphone_std"],
            "microphone_variance": datos["microphone_variance"],
            "acc_under_tangencial_variance": datos["acc_under_tangencial_variance"],
            "acc_under_tangencial_std": datos["acc_under_tangencial_std"],
            "acc_under_radiale_range": datos["acc_under_radiale_range"],
            "acc_under_radiale_mean": datos["acc_under_radiale_mean"],
            "acc_under_axial_skewness": datos["acc_under_axial_skewness"],
            "acc_over_axial_dominant_frequency": datos["acc_over_axial_dominant_frequency"],
            "acc_over_radiale_median": datos["acc_over_radiale_median"],
            "acc_over_axial_skewness": datos["acc_over_axial_skewness"],
            "acc_over_tangencial_kurtosis": datos["acc_over_tangencial_kurtosis"],
            "acc_over_tangencial_skewness": datos["acc_over_tangencial_skewness"],
            "acc_over_radiale_dominant_frequency": datos["acc_over_radiale_dominant_frequency"]
        }

        # Llamada POST al servicio de predicción
        response_para_predict = requests.post(url_prediccion, json=features)
        if response_para_predict.status_code == 200:
            pred = response_para_predict.json()
            
            # Formar el objeto final que enviaremos a Kafka
            kafka_data = {
                "features": features,
                "prediction": pred
            }
            
            # Enviar a Kafka (sin 'id' porque no existe en los datos)
            producer.produce(
                'flask_topic',
                value=json.dumps(kafka_data),
                callback=acked
            )

        # Fuerza envío del message
        producer.flush()
    else:
        # Rompe el bucle si el endpoint no responde 200
        break
