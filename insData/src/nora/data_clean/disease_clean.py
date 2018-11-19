import pandas as pd
import re


def get_disease_count():
    split_pattern_list = ['{|', '}', ',', '、', '，', '；', ';', '（', '）', '\(', '\)', '.', '。', '\s', '-', '－', '｛']
    df = pd.read_csv('/Users/zhaoning/Documents/project/dataMining/userIntent/insData/res/data/disease_yiqing.csv')
    save = open(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/test.txt', 'w',
        encoding='utf-8')
    df_series = df['疾病的集合']
    disease_set_dict = {}
    for index, diseases_row in df.iterrows():
        diseases = diseases_row['疾病的集合']
        disease_list = re.split(r'{|}|"|,|、|，|；|;|（|）|\(|\)|\.|。|\s|—|｛|－', str(diseases))
        # print(disease_list)
        for disease_item in disease_list:
            # print(disease_item)
            if disease_item not in split_pattern_list:
                if disease_set_dict.__contains__(disease_item):
                    disease_set_dict[disease_item] = disease_set_dict[disease_item] + 1
                else:
                    disease_set_dict[disease_item] = 1
    # print(disease_set_dict)
    sorted_array = sorted(disease_set_dict.items(), key=lambda item: item[1])
    sorted_array.reverse()
    # print(sorted_array)
    disease = []
    count = []
    for key, value in sorted_array:
        disease.append(key)
        count.append(value)
    df_res = pd.DataFrame(data={'disease': disease, 'count': count})
    df_res.to_csv(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/disease_count.csv')
    print(df_res, file=save)


def get_disease_list():
    diseases_redun_str = ['不详', '疾病', '肿瘤', '重大疾病', '特定疾病', '畸形', '并发']
    save = open(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/test.txt', 'w',
        encoding='utf-8')
    list = []
    df = pd.read_csv(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/disease_count.csv').dropna()
    for index, diseases_row in df.iterrows():
        if 1 < diseases_row['count'] < 20 \
                and diseases_row['disease'] not in diseases_redun_str \
                and len(diseases_row['disease']) > 1:
            list.append(diseases_row['disease'])
    for item in list:
        print(item, file=save)
    # print(len(list), list, file=save)


def get_insurance_period():
    df = pd.read_csv('/Users/zhaoning/Documents/project/dataMining/userIntent/insData/res/data/disease_yiqing.csv')
    df_series = df['保险期间']
    save = open(
        '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/test.txt', 'w',
        encoding='utf-8')
    set_period = set()
    for index, diseases_row in df.iterrows():
        if diseases_row['保险期间'] != '不详':
            set_period.add(diseases_row['保险期间'])
    for item in set_period:
        print(item, file=save)


# 获得疾病集合的txt
# get_disease_count()
# get_disease_list()

# 获得保险期间
get_insurance_period()
