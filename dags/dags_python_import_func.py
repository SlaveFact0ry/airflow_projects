from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025,9,20, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    
) as dag:


    take_get_sftp = PythonOperator(
        task_id = 'get_sftp',
        python_callable=get_sftp
    )
    take_get_sftp