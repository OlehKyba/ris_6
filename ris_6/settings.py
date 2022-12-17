import os


MONGO_URI = os.getenv(
    'MONGO_URI',
    'mongodb://root:password123@mongodb-sharded:27017/?authSource=admin',
)
MONGO_DB = os.getenv('MONGO_DB', 'ris_6')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'dataset')

DATASET_PATH = os.getenv('DATASET_PATH', './data/dataset.csv')
