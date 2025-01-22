from confluent_kafka import Consumer, KafkaException
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['flask_topic'])

output_data = []
url = 'http://127.0.0.1:5000/predict'

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                break
            else:
                print(f"Error: {msg.error()}")
                continue
        record = json.loads(msg.value().decode('utf-8'))
        
        print(f"Recibido: {record}")
        output_data.append(record)
        '''
        try:
            response = requests.post(url, json=record)
            if response.status_code == 200:
                print(f"Predicción: {response.json()}")
            else:
                print(f"Error en la predicción: {response.status_code}, {response.text}")
        except requests.RequestException as e:
            print(f"Error al conectar con el simulador: {e}")
        '''
        #if len(output_data) == 10:  # Limitar a 10 mensajes, cambia según sea necesario
         #   break  #Hemos hecho prueba de que con 10 iba, vamos a comentar ambas lineas y ver el resultado final
except KeyboardInterrupt:
    pass
finally:
    # Guardar datos en un archivo JSON
    with open('prediccion_series_temporales.json', 'a') as f:
        json.dump(output_data, f, indent=4)
    consumer.close()
    print(len(output_data))
