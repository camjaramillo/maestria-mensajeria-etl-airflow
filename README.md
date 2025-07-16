# Maestría en Analítica e Inteligencia de Negocios
## Curso Introducción a la Ingeniería de Datos y Big Data

### Proyecto Mensajería - ETL

<hr>

## Despliegue del proyecto con Docker

<br>1. Ejecutar el Dockerfile</br>

docker build -t mensajeria-airflow-image .

Al hacer esto, se creara la imagen mensajeria-airflow-image en Docker.


<br>2. Iniciar la base de datos de Airflow (una sola vez)</br>

docker compose up airflow-init

<br>3. Iniciar todos los contenedores para ejecutar Airflow</br>

docker-compose up


<br>(opc) Iniciar los servicios principales de AirFlow</br>

docker compose up -d airflow-webserver airflow-scheduler

<br>4. Detener todos los contenedores de Airflow</br>

Para detener el despliegue del proyecto, ejecutar:

docker-compose stop

O para eliminar los contenedores

docker-composer down