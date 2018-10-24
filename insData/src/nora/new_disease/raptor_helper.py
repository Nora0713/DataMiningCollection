import pandas as pd
import re


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


get_all_attributions()
