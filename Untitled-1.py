import json
from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch("http://localhost:9200")
es.indices.delete(index='my-index', ignore_unavailable=True)
es.indices.create(index='my-index')


def insert_document(document):
    response = es.index(index='my_index', document=document)
    return response

def print_info(response): 
    print(f"Document ID: {response['_id']} is '{response['result']}' and is split into {response['_shards']['total']} shards.")

# document = {'title': 'something'}

# response = insert_document(document)

dummy_data = json.load(open("./dummy_data.json"))
# pprint(dummy_data)

for document in dummy_data: 
    response = insert_document(document)
    print_info(response)

index_mapping = es.indices.get_mapping(index="my_index")
pprint(index_mapping['my_index']['mappings']['properties'])