# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re

# %matplotlib inline  # 为了在jupyter notebook里作图，需要用到这个命令
disease_set_package_file = "../../res/data/disease_set_package1.csv"
disease_set_dict = {}
disease_set_invalid_count = 0

df = pd.read_csv(disease_set_package_file)
df_series = df['疾病集合']

for index, disease_set in df.iterrows():
    diseases = str(disease_set['疾病集合'])
    disease_list = re.split('{|}|"|,|、|，|；|;', diseases)
    for disease_item in disease_list:
        # print(disease_item)
        if disease_item != '{' and disease_item != '}' and disease_item != '' and disease_item != ';' and disease_item != '；' and disease_item != '，' and disease_item != ',':
            if disease_set_dict.__contains__(disease_item):
                disease_set_dict[disease_item] = disease_set_dict[disease_item] + 1
            else:
                disease_set_dict[disease_item] = 1
print(disease_set_dict)
sorted_array = sorted(disease_set_dict.items(), key=lambda item: item[1])
sorted_array.reverse()
print(sorted_array)

disease = []
count = []
for key, value in sorted_array:
    disease.append(key)
    count.append(value)
df_res = pd.DataFrame(data={'disease': disease, 'count': count})
df_res.to_csv('disease_set.csv')
# disease_set_dict[''] = disease_set_dict[]

# start_age = []
# end_age = []
# start_age_count_list = []
# end_age_count_list = []
#
# df = pd.read_csv(age_segment_file)['投保范围_开始年龄结束年龄']
# # df.to_csv('temp.csv')
# age_range_sum = df.count()
# age_range_data_none = df[df.str.contains('无')].count()
# age_range_data_strange = df[df.str.contains('特殊数据')].count()
#
# df_valid = df[(~df.str.contains('无') & ~df.str.contains('特殊数据'))]
# df_valid.to_csv('temp.csv')
# # for i in range(age_segment_list.__len__()):
# for ages in df_valid:
#     start_age.append(ast.literal_eval(ages)[2])
#     end_age.append(ast.literal_eval(ages)[3])
# print(end_age)
# df_age = pd.DataFrame(data={'start_age': start_age, 'end_age': end_age}).fillna(' ')
# df_age.to_csv('temp.csv')
# df_start_age = pd.Series(df_age['start_age'])
# df_end_age = pd.Series(df_age['end_age'])
# print(df_end_age)
# for i in range(age_segment_list.__len__()):
#     age_segment = age_segment_list[i]
#     start_age_count_list.append(df_start_age[df_start_age.str.contains(age_segment)].count())
#     end_age_count_list.append(df_end_age[df_end_age.str.contains(age_segment)].count())
# print(len(start_age_count_list), len(end_age_count_list), len(age_segment_list))
# df_charts = pd.DataFrame(data={'age_segment': age_segment_list, 'start_age_count': start_age_count_list,
#                                'end_age_count': end_age_count_list})
# print(df_charts)
# # bar=pyecharts.Bar("标注情况")
# # age_list=list(df_charts[df_charts.columns[0]])
# # bar.add('分布',df_charts.index,df_charts['age_segment_count'],mark_line=['average'],is_stack=True,xaxis_type='category',xaxis_interval=1,)
