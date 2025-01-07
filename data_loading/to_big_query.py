from google.cloud import bigquery
import pandas as pd

# Configurações
project_id = "pipeline-projeto-vendas"
dataset_id = "sales_data"  # Substitua pelo nome do seu dataset
table_id = "transformed_sales"  # Nome da tabela no BigQuery

# Caminho para o arquivo CSV transformado
csv_path = "etl-pipeline-projeto-vendas/data_transformation/transformed_data/transformed_sales_data.csv"

# Inicializar cliente BigQuery
client = bigquery.Client()

# Carregar dados CSV para um DataFrame
print("Carregando dados do CSV...")
df = pd.read_csv(csv_path)

# Configurar esquema (opcional)
schema = [
    bigquery.SchemaField("sale_id", "STRING"),
    bigquery.SchemaField("customer_name", "STRING"),
    bigquery.SchemaField("customer_email", "STRING"),
    bigquery.SchemaField("product", "STRING"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("price_per_unit", "FLOAT"),
    bigquery.SchemaField("sale_date", "DATE"),
    bigquery.SchemaField("total_revenue", "FLOAT"),
    bigquery.SchemaField("price_category", "STRING"),
]

# Configurar job de carregamento
table_ref = f"{project_id}.{dataset_id}.{table_id}"
job_config = bigquery.LoadJobConfig(
    schema=schema,
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=False,
)

# Enviar dados para o BigQuery
print(f"Carregando dados para {table_ref}...")
with open(csv_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file, table_ref, job_config=job_config
    )
job.result()  # Esperar o job completar

print(f"Dados carregados com sucesso em {table_ref}.")
