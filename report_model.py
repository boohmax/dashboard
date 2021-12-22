import pandas as pd
import json


def collect_model_data():
    file = open("option_3S3.json")
    option = json.load(file)
    file.close()

    model_url = option[0]['Model_sheet']\
        .replace('/edit#gid=', '/export?format=csv&gid=')
    
    Model_data = pd.read_csv(model_url)
    Model_list = Model_data[['DP', 'Выдано', 'Модель',\
        'чертежи', 'МС', 'ревизия', 'First Issuance Forecast date']]
    Model_list = Model_list.fillna('None')
    
    Model_list = Model_list.reset_index(drop=True)

    return Model_list
