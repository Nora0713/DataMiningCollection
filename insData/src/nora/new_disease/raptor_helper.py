import pandas as pd
import json


def get_all_attributions():
    label_json = {"type": "entity", "label": []}
    # print(label_json['label'])
    save_label = open(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/file/label.json', 'w',
        encoding='utf-8')
    df_sttr = pd.read_csv(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/file/结构属性1015-新结构.csv')
    series_attr = df_sttr['结构小项']
    # print(series_attr)
    for attr in series_attr:
        # pattern = re.compile('\d*\.\d*\.*\d*\.*\d*\.*(\D*)')
        # res = re.match(pattern, str(attr))
        # print(attr, res.group(1))
        # new_attr = res.group(1)
        label_json['label'].append(attr)
    print(str(label_json).replace('\'', '"'), file=save_label)


def get_new_labels():
    with open(
            '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/file/label_relation_new.json',
            encoding='utf-8-sig') as j:
        save = open(
            '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/new_disease/test.txt', 'a+',
            encoding='utf-8')
        lines = j.readlines()
        json_raw_string = ""
        for line in lines:
            json_raw_string = json_raw_string + line
        data = json.loads(json_raw_string)
        labels = data['label']
        entity2_labels = []
        for item in labels:
            if item['label_front'] not in entity2_labels:
                entity2_labels.append(item['label_front'])
            if item['label_after'] not in entity2_labels:
                entity2_labels.append(item['label_after'])
        entity2_labels.sort()
        for item in entity2_labels:
            print('"'+item+'",', file=save)


get_new_labels()
