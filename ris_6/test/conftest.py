import pytest
from pymongo import MongoClient
from pymongo.database import Database, Collection

from ris_6.settings import MONGO_URI, MONGO_DB, MONGO_COLLECTION
from ris_6.bl import init_sharding


@pytest.fixture
def mongo_client() -> MongoClient:
    client = MongoClient(MONGO_URI)
    return client


@pytest.fixture
def admin_db(mongo_client: MongoClient) -> Database:
    db = mongo_client['admin']
    return db


@pytest.fixture
def dataset_collection(
    mongo_client: MongoClient,
    admin_db: Database,
) -> Collection:
    init_sharding(admin_db)

    ris_6_db = mongo_client[MONGO_DB]
    dataset_coll = ris_6_db[MONGO_COLLECTION]

    try:
        yield dataset_coll
    finally:
        ris_6_db.drop_collection(MONGO_COLLECTION)
        mongo_client.drop_database(MONGO_DB)
