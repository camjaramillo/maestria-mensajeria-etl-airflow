# Usa la imagen base oficial de Airflow
FROM apache/airflow:2.9.1

# Copia el archivo de requerimientos
COPY ./etl_app/requirements.txt /requirements.txt

# Instala los requerimientos
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
