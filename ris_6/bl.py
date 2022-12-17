import csv

from pymongo import MongoClient
from pymongo.database import Database, Collection

from ris_6.settings import MONGO_DB, MONGO_COLLECTION, DATASET_PATH


def init_sharding(
    admin_db: Database,
    db_name: str = MONGO_DB,
    collection_name: str = MONGO_COLLECTION,
) -> None:
    admin_db.command('enableSharding', db_name)
    admin_db.command(
        {
            'shardCollection': f'{db_name}.{collection_name}',
            'key': {'sex': 'hashed'},
        },
    )


def load_dataset(
    dataset_collection: Collection,
    dataset_path: str = DATASET_PATH,
) -> None:
    with open(dataset_path) as file:
        reader = csv.DictReader(file)
        dataset_collection.insert_many(
            [
                row for row in reader
            ]
        )


def fetch_shards_info(
    client: MongoClient,
    db_name: str = MONGO_DB,
) -> dict:
    info = {}
    for doc in client.list_databases():
        if doc['name'] == db_name:
            info = doc['shards']
            break

    return info
