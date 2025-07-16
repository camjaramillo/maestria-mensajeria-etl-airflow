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
        ["python", "/opt/airflow/etl_app/main.py", "--etl", "dim_tipo_servicio", "--start_date", datetime.now().strftime("%Y-%m-%d")],
        check=True
    )

with DAG(
    dag_id='etl_dim_tipo_servicio',
    schedule_interval=None,
    default_args=default_args,
    description='Ejecuta solo el ETL de dim_tipo_servicio',
    tags=['etl', 'dim_tipo_servicio']
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_dim_tipo_servicio',
        python_callable=run_etl
    )
