# Una Solución Integral para Mantenimiento Predictivo

## Descripción

El objetivo de este proyecto es desarrollar un sistema integral de mantenimiento predictivo basado en inteligencia artificial (IA) para maximizar la disponibilidad operativa de los componentes y reducir los costos de mantenimiento. Combina análisis de series temporales, visión artificial y aprendizaje automático en una plataforma unificada y escalable.

## Estructura del Repositorio

- **Imagenes_defectos/**: Contiene imágenes microscópicas de piezas defectuosas, incluidas máscaras de anotación por píxeles. Estas imágenes permiten identificar si existen defectos y dónde se encuentran.
- **bearing_fault_detection_reduced/**: Incluye datos y scripts relacionados con la detección de fallos en rodamientos, clasificando los tipos de fallos (desequilibrio, desalineación, anillo exterior/interior, etc.).
- **kafka/**: Contiene la arquitectura para la ingesta y almacenamiento de datos en tiempo real utilizando Apache Kafka, esencial para la escalabilidad del sistema.
- **modelos_clasificacion_imagenes/**: Modelos y scripts para el análisis y clasificación de imágenes, aplicados a la detección de defectos en piezas.
- **segmentacion/**: Scripts para segmentar imágenes y localizar defectos específicos en áreas relevantes.
- **series_temporales/**: Scripts y datos para el análisis de series temporales, que ayudan a predecir y detectar anomalías en señales de sensores de producción.
- **README.md**: Este archivo, que proporciona una visión general del proyecto.

## Requisitos

- Python 3.12
- Librerías especificadas en los códigos.

## Instalación

1. Clona este repositorio:
   git clone https://github.com/joanesMondra/reto2.git
   
3. Navega al directorio del proyecto:
  cd reto2
  
3. Instala las dependencias necesarias:
  pip install "las librerías necesarias"

## Uso
## Clasificación de imágenes:

1. En la carpeta modelos_clasificacion_imagenes\simpleCNN_clasificator lanzar dataAugmentation.py
2. Elegir entre los distintos modelos presentes en modelos_clasificacion_imagenes: resnet18 o model_clasificator (CNN simple)
3. Ejecutar el modelo seleccionado (resnet18_con_aumento.ipynb, resnet18_sin_aumentar .ipynb o model_clasificator.ipynb)
4. Para hacer test con nuevos datos generar una copia de la carpeta Imagenes_defectos y repertir paso 1 cambiando el root_dir con la ubicación y nombre de nuestra carpeta creada
5. Ejecutar el archivo testModelo.ipynb cambiando el "new_data_dir" al directorio de los nuevos datos y cambiando el "path" a el nombre con el que has guarado el modelo en el paso 3, ejemplo path="simple_cnn_model_data_aug.pkl"

## Clasificación de errores mediante series temporales y Kafka:

1. En la carpeta series_temporales crear el archivo con los estadísticos mediante crear_excel_full.py
2. Elegir el modelo que se quiere implementar: SVM o Random Forest
3. Ejecutar el modelo modelo_subcategorias_RF.ipynb (o modelo_subcategoria_SVM.ipynb)
4. Para el simulador Kafka, entrar en la carpeta Kafka.
5. En un terminal poner en marcha el zookeper y Kafka: ./bin/zookeeper-server-start.sh ./config/zookeeper.properties  y  ./bin/kafka-server-start.sh config/server.properties
6. Lanzar el simulador (simulador_ejercicio.py) y producer (producer_ejercicio.py)
7. Lanzar el consumer (consumer_ejercicio.py) para obtener prediccion_series_temporales.json

## Localización del error:

1. En la carpeta segmentacion, asegúrate de que el archivo unet.pkl esté descargado y disponible.
2. Abre el notebook segmentacion_errores.ipynb.
3. Configura el notebook según las instrucciones proporcionadas en las celdas iniciales, asegurándote de que el directorio de las imágenes de entrada esté correctamente especificado.
4. Ejecuta el notebook paso a paso para cargar el modelo entrenado (unet.pkl) y realizar la segmentación en las imágenes proporcionadas.
5. Los resultados de la segmentación se guardarán en la carpeta especificada dentro del notebook, con las máscaras generadas para los defectos detectados.
6. Verifica las máscaras generadas para analizar y validar la localización precisa de los defectos en las imágenes.

## Créditos
Desarrollado por Joanes De Miguel, Esteban Ruiz y Hodei Azurmendi

## Contacto
Para cualquier pregunta, comentario o sugerencia, por favor contacta al desarrollador principal a través de GitHub.
