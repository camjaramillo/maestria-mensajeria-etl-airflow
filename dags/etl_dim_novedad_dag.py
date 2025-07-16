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
        ["python", "/opt/airflow/etl_app/main.py", "--etl", "dim_novedad", "--start_date", datetime.now().strftime("%Y-%m-%d")],
        check=True
    )

with DAG(
    dag_id='etl_dim_novedad',
    schedule_interval=None,
    default_args=default_args,
    description='Ejecuta solo el ETL de dim_novedad',
    tags=['etl', 'dim_novedad']
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl_dim_novedad',
        python_callable=run_etl
    )
