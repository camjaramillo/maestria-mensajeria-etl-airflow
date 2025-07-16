from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

with DAG(
    dag_id='etl_full_pipeline',
    schedule_interval=None, #min 0, hora 7, diario
    #schedule_interval='0 7 * * *', #min 0, hora 7, diario
    default_args=default_args,
    description='Ejecuta el ETL directamente desde el contenedor de Airflow',
    tags=['etl']
) as dag:

    run_etl = BashOperator(
        task_id='run_etl_locally',
        bash_command='python /opt/airflow/etl_app/main.py --start_date 2023-01-01'
        #bash_command='python /opt/airflow/etl_app/main.py --start_date {{ ds }}'
    )
