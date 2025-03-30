from elasticsearch import Elasticsearch, helpers
import csv

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

index_name = "public_dataset"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body={
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
             # Add additional mappings as per your dataset columns
             "properties": {
                "index": {"type": "integer"},
                "first_name": {"type": "text"},
                "last_name": {"type": "text"},
                "sex": {"type": "keyword"},
                "email": {"type": "keyword"},
                "phone": {"type": "keyword"},
                "date_of_birth": {"type": "date", "format": "dd-MM-yy"},
                "job_title": {"type": "text"}
            }
        }
    })

def transform_row(row):
    return {
        "index": int(row["Index"]) if row["Index"].isdigit() else None,
        "first_name": row["First Name"],
        "last_name": row["Last Name"],
        "sex": row["Sex"],
        "email": row["Email"],
        "phone": row["Phone"],
        "date_of_birth": row["Date of birth"],
        "job_title": row["Job Title"]
    }

def generate_actions(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Transform row keys to match the mapping
            doc = transform_row(row)
            yield {
                "_index": index_name,
                "_source": doc
            }

csv_file_path = "app/employee.csv"
# DOWNLOADED FROM: https://www.kaggle.com/datasets/zahidmughal2343/employee-data?resource=download

success, failed = helpers.bulk(es, generate_actions(csv_file_path), raise_on_error=False)
print(f"Successfully indexed {success} documents. Failed {failed} documents.")
