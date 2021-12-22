import report_DP
import report_model
import math


def nest_list(list1, columns):
        result=[]
        start = 0
        end = columns
        for i in range(int(math.ceil(len(list1)/columns))):
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result


def load_data_DP():
    data = report_DP.collect_data().T.to_dict()
    list_DP = []
    for d in data.values():
        list_DP.append(d)
    return list_DP


def load_data_model():
    data = report_model.collect_model_data().T.to_dict()
    list_model = []
    for d in data.values():
        list_model.append(d)
    return list_model


def restructed_data_DP(list_DP):
    restructed_data = []
    data_for_use = []

    for dp in list_DP:
        new_dict = {}
        new_dict['DP'] = dp['DP']
        if dp['type'] == 'D':
            new_dict['DRW_D'] = dp['Чертеж']
            new_dict['DRW_D_all'] = dp['№черт.']
        if dp['type'] == 'M':
            new_dict['DRW_M'] = dp['Чертеж']
            new_dict['DRW_M_all'] = dp['№черт.']
        if dp['type'] == 'SA':
            new_dict['DRW_SA'] = dp['Чертеж']
            new_dict['DRW_SA_all'] = dp['№черт.']
        restructed_data.append(new_dict)

    for x in range(len(restructed_data)-1):
        if restructed_data[x]['DP'] == restructed_data[x+1]['DP']:
            restructed_data[x+1] = {**restructed_data[x], **restructed_data[x+1]}
            restructed_data[x] = None

    for dp in restructed_data:
        if dp not in data_for_use and dp != None:
            data_for_use.append(dp)

    return data_for_use
