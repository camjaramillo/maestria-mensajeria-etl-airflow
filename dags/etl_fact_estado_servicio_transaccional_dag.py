from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

def run_etl():
    subprocess.run(
        ["python", "/opt/airflow/etl_app/main.py", "--etl", "fact_estado_servicio_transaccional", "--start_date", "2023-01-01"],
        check=True
    )

with DAG(
    dag_id='etl_fact_estado_servicio_transaccional',
    schedule_interval=None,
    default_args=default_args,
    description='Ejecuta solo el ETL de fact_estado_servicio_transaccional',
    tags=['etl', 'fact_estado_servicio_transaccional']
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_fact_estado_servicio_transaccional',
        python_callable=run_etl
    )
