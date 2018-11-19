import json
from os import listdir
from os.path import isfile, join
import pandas as pd

raw_res_data_dirpath = './reg_output'
df_user_labeling_result = pd.DataFrame(columns=('username', 'files_count', 'labels_count', 'avg_labels_count'))
df = pd.DataFrame(columns=('username', 'files_count', 'labels_count', 'avg_labels_count'))
labels_set = set()


def read_json(filepath):
    with open(filepath, encoding='utf-8-sig') as j:
        try:
            lines = j.readlines()
            json_raw_string = ""
            for line in lines:
                json_raw_string = json_raw_string + line
            data = json.loads(json_raw_string)
            return data
        except Exception:
            print(filepath)


def read_dir(dirname):
    onlyfiles = [f for f in listdir(dirname) if isfile(join(dirname, f))]
    return onlyfiles


def stat_user_labeling():
    global df_user_labeling_result
    for f in read_dir(raw_res_data_dirpath):
        username = f[:-10]
        # print(username)
        filepath = './任务导出结果/' + f
        data = read_json(filepath)
        files_count = 0
        spans_count = 0
        for data_set in data['result']:
            per_spans_count = len(data_set['spans'])
            spans_count += per_spans_count
            if per_spans_count > 0:
                files_count += 1
            # if df_user_labeling_result[df_user_labeling_result['username']
            #         .str.contains(username, case=False, na=False)].empty:
        df_user_labeling_result.loc[df_user_labeling_result.shape[0] + 1] = [username, files_count, spans_count, 0]
        # else:
        #     row = df_user_labeling_result.loc[df_user_labeling_result.loc[:, "username"] == username, :]
        #     df_user_labeling_result.loc[
        #         df_user_labeling_result.loc[:, "username"] == username, 'files_count'] = files_count + row[
        #         'files_count']
        #     df_user_labeling_result.loc[
        #         df_user_labeling_result.loc[:, "username"] == username, 'labels_count'] = spans_count + row[
        #         'labels_count']
        #     df_user_labeling_result.loc[df_user_labeling_result.loc[:, "username"] == username, 'avg_labels_count'] = \
        #         row['labels_count'] / row['files_count']
        # if username == '徐佳庆':
        #     print(spans_count, df_user_labeling_result.loc[
        #                        df_user_labeling_result.loc[:, "username"] == username, :])
    df_user_labeling_result.to_csv('./user_labeling_result.csv')
    #
    df = df_user_labeling_result.groupby(df_user_labeling_result['username']) \
        .agg({'files_count': 'sum', 'labels_count': 'sum'}).reset_index()
    # .rename(columns={'Organisation Name': 'Organisation Count'})
    df.to_csv('./user_labeling_result.csv')


if __name__ == '__main__':
    stat_user_labeling()
