import pandas as pd
from pandas import Series, DataFrame


class OptExcel:
    # def __init__(self):

    def change_schema(self):
        df_raw = pd.read_excel("/Users/zhaoning/Desktop/里程数.xlsx")
        df_raw.rename(columns={'Unnamed: 0': 'train_num'}, inplace=True)
        df_raw.set_index('train_num', inplace=True)
        df = DataFrame(index=['id'], columns=['train_num', 'date', 'value'])
        i = 1
        for train_num in df_raw.index:
            # print(train_num)
            for date in df_raw.columns.values:
                value = df_raw.loc[train_num, date]
                df.loc[i] = [train_num, str(date), value]
                i += 1
        print(df)
        df.to_excel('/Users/zhaoning/Desktop/里程数_res.xlsx',sheet_name='里程数')


if __name__ == "__main__":
    pe = OptExcel()
    pe.change_schema()
