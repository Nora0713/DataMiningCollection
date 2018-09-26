import os
import pandas as pd
import numpy as np


# 分离5w和1w的数据

class DataSegmentation:
    def __init__(self):
        self.raw_data_file_path_6w = "../res/riskeys_records_ask.xlsx"
        self.raw_data_file_6w_sheet = "riskeys-back_records_ask"
        self.raw_data_file_path = "../res/riskey_data_100.xlsx"
        self.raw_data_file_sheet = "Sheet1"
        self.result_5w_data = "../res/result/riskeys_ask_data_5w.csv"
        self.result_2k_data = "../res/result/riskeys_ask_data_2k.csv"

    def clean_data(self, df_data):
        df_cleaned_data = df_data.fillna(-1).replace({'\n': 0})
        return df_cleaned_data

    def split_5w_data(self):
        df_riskeys_ask_data = pd.read_excel(self.raw_data_file_path_6w)
        df_riskeys_ask_test_data = pd.read_excel(self.raw_data_file_path)
        df_5w = df_riskeys_ask_data[df_riskeys_ask_data['userId'].isin(['oeDaQxGWMb3iSHKSRvvC6RlMK89Y'])]
        df_5w.index = range(len(df_5w))
        self.clean_data(df_5w).to_csv(self.result_5w_data)

    def split_2k_data(self):
        df_riskeys_ask_data = pd.read_excel(self.raw_data_file_path_6w)
        # df_riskeys_ask_data[['platform', 'id']].groupby('platform').count().to_csv('../res/result/platform_group.csv')
        df_2k = df_riskeys_ask_data[~df_riskeys_ask_data['userId'].isin(['oeDaQxGWMb3iSHKSRvvC6RlMK89Y'])]
        df_2k.index = range(len(df_2k))
        self.clean_data(df_2k).to_csv(self.result_2k_data)


if __name__ == '__main__':
    ds = DataSegmentation()
    ds.split_2k_data()
    ds.split_5w_data()
