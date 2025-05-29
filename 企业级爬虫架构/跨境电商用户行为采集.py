# 使用Airflow实现数据隔离管道
from airflow import DAG
from airflow.operators.docker import DockerOperator

with DAG('gdpr_pipeline') as dag:
    extract = DockerOperator(image='extractor', command='--zone=eu')
    transform = DockerOperator(image='anonymizer', command='--level=strict')
    load = DockerOperator(image='loader', command='--storage=encrypted')
    extract >> transform >> load
