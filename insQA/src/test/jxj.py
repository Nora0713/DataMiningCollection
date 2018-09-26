import os
import pandas as pd
import numpy as np


class Analyse:
    def __init__(self):
        self._18file = "/Users/zhaoning/Documents/project/dataMining/userIntent/insQA/res/jxj/2017-2018学年绩点排名公示（不含挂科学生）.xlsx"
        self._17file = "/Users/zhaoning/Documents/project/dataMining/userIntent/insQA/res/jxj/mua.xlsx"

    def match_stu(self):
        df_17_file = pd.read_excel(self._17file)
        df_18_file = pd.read_excel(self._18file)
        list_18_num = df_18_file['学号后四位']
        list_17_num = df_17_file
        df_17_file[df_17_file.filter()]
        print(list_18_num)
        for num in list_18_num:
            name = list_17_num['学号']
        # print(df_riskeys_ask_data.count())
        # df_riskeys_ask_data[['学号后四位']].groupby('platform').count().to_csv('../res/result/platform_group.csv')


if __name__ == '__main__':
    al = Analyse()
    al.match_stu()
