from time import sleep

from pymongo import MongoClient
from pymongo.database import Collection

from ris_6.bl import load_dataset, fetch_shards_info


def test_mongodb_sharding(
    mongo_client: MongoClient,
    dataset_collection: Collection,
) -> None:
    load_dataset(dataset_collection)
    # Give 5 seconds for sharding sync
    # sleep(5)

    shards_info = fetch_shards_info(mongo_client)
    shard_0_size = shards_info.get('shard0', 0)
    shard_1_size = shards_info.get('shard1', 0)

    assert shard_0_size > 0
    assert shard_1_size > 0
