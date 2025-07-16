import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from src.utils.database import db_session, DBConnection
from src.utils.logger import logger

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

# Lista de tablas de staging que se deben purgar
STAGING_TABLES = [
    'stg_dim_cliente',
    'stg_dim_estado_servicio',
    'stg_dim_fecha',
    'stg_dim_hora',
    'stg_dim_mensajero',
    'stg_dim_novedad',
    'stg_dim_sede',
    'stg_dim_tipo_servicio',
    'stg_fact_estado_servicio_transaccional',
    'stg_fact_novedad_servicio_transaccional',
    'stg_fact_servicio'
]

def backup_and_purge_tables():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    backup_folder = f"/opt/airflow/backups/backup_{timestamp}"
    os.makedirs(backup_folder, exist_ok=True)

    with db_session(DBConnection.STAGING) as session:
        logger.info(f'***********************************************************************')
        logger.info(f'******************** Respaldando tablas de staging ********************')
        logger.info(f'***********************************************************************')

        for table in STAGING_TABLES:
            logger.info(f"Respaldando tabla: {table}")
            try:
                df = pd.read_sql(f"SELECT * FROM {table}", session.bind)
                csv_path = os.path.join(backup_folder, f"{table}.csv")
                df.to_csv(csv_path, index=False)
                logger.info(f"Backup creado: {csv_path}")
            except Exception as e:
                logger.error(f"Error al respaldar la tabla {table}: {e}")

        logger.info(f'***********************************************************************')
        logger.info(f'********************* Limpiando tablas de staging *********************')
        logger.info(f'***********************************************************************')

        for table in STAGING_TABLES:
            logger.info(f"Purgando tabla: {table}")
            try:
                session.execute(f"DELETE FROM {table}")
                logger.info(f"Tabla purgada: {table}")
            except Exception as e:
                logger.error(f"Error al purgar la tabla {table}: {e}")

with DAG(
    dag_id='purge_staging_tables_with_backup',
    description='Respaldar y purgar tablas STAGING periódicamente',
    schedule_interval=None,
    #schedule_interval='0 3 * * 1',  # min 0, hora 0, cualquier dia *, cualquier mes *, dia lunes 1 
    default_args=default_args,
    tags=['purga', 'backup'],
) as dag:

    purge_task = PythonOperator(
        task_id='backup_and_purge_staging',
        python_callable=backup_and_purge_tables,
    )
