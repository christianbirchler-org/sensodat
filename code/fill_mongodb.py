from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path
import json
import os
import re
import xmltodict


uri = "mongodb://msr:fooBar@{}:27017/?authMechanism=DEFAULT".format(os.getenv('MONGO_IP'))

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def write_collection(_data_path: Path, mongodb_collection):

    for file in os.listdir(_data_path):
        if 'sim_data' in file:
            continue
        m = re.match(r"(\d\d\d\d\d)-test.xodr", file)
        try:
            test_id = m.group(1)
        except:
            continue

        xodr_file_path = _data_path / file
        if not xodr_file_path.exists():
            continue
        with open(xodr_file_path, 'r') as fp:
            xodr_dict = xmltodict.parse(fp.read())

        sim_file_name = str(test_id) + '-test_sim_data.json'
        sim_file_path = _data_path / 'sim_data' / sim_file_name
        if not sim_file_path.exists():
            continue
        with open(sim_file_path, 'r') as fp:
            sim_data_dict = json.load(fp)

        xodr_dict['execution_data'] = sim_data_dict

        mongodb_collection.insert_one(xodr_dict)


sdc_sim_db = client['sdc_sim_data']

data_path = Path('../data/')

for key, data_dir_name in enumerate(sorted(os.listdir(data_path))):
    if 'README.md' in data_dir_name or 'data.zip' in data_dir_name:
        continue
    campaign_name = 'campaign_{}'.format(key)
    high_level_data_dir = data_path / data_dir_name / data_dir_name
    for tool_dir in os.listdir(high_level_data_dir):
        collection_name = campaign_name + '_' + str(tool_dir)
        mongodb_collection = sdc_sim_db[collection_name]
        print('Write collection: {}'.format(collection_name))
        write_collection(high_level_data_dir / str(tool_dir), mongodb_collection)
    

