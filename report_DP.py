import pandas as pd
import json


def extract_drw_type(drw):
    if isinstance(drw, str):
        if len(drw) == 37:
            return drw[31:32]
        else:
            return drw[31:33]
    else:
        return drw


def collect_data():
    file = open("option_3S3.json")
    option = json.load(file)
    file.close()

    D_url = option[0]['D_sheet'].replace('/edit#gid=', '/export?format=csv&gid=')
    M_url = option[0]['M_sheet'].replace('/edit#gid=', '/export?format=csv&gid=')
    SA_url = option[0]['SA_sheet'].replace('/edit#gid=', '/export?format=csv&gid=')

    D_data = pd.read_csv(D_url)
    M_data = pd.read_csv(M_url)
    SA_data = pd.read_csv(SA_url)
    D_list = D_data[['№черт.', 'DP', 'Чертеж']]
    M_list = M_data[['№черт.', 'DP', 'Чертеж']]
    SA_list = SA_data[['№черт.', 'DP',  'Чертеж']]

    all_data = D_list.append(M_list).append(SA_list)
    all_data['type'] = all_data['№черт.'].apply(extract_drw_type)

    report_DP = all_data.pivot_table(
        index=['DP', 'type'],
        values=['Чертеж', '№черт.'],
        aggfunc='count'
        )

    report_DP = report_DP.reset_index()

    return report_DP
