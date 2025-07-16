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
        ["python", "/opt/airflow/etl_app/main.py", "--etl", "dim_mensajero", "--start_date", datetime.now().strftime("%Y-%m-%d")],
        check=True
    )

with DAG(
    dag_id='etl_dim_mensajero',
    schedule_interval=None,
    default_args=default_args,
    description='Ejecuta solo el ETL de dim_mensajero',
    tags=['etl', 'dim_mensajero']
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_dim_mensajero',
        python_callable=run_etl
    )
