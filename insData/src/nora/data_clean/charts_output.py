import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class ChartsOutput:
    def __init__(self):
        self.disease_raw = "../res/data/disease_edit.csv"
        self.age_segment_file = "../res/data/age_segment_file.csv"
        self.disease_yiqing = "../res/data/disease_yiqing.csv"
        self.disease_set_package = "../res/data/disease_set_package.csv"
        self.age_segment_list = ['0岁', '1-7天', '8-15天', '16-27天', '28-30天', '31-50天', '50天-364天', '1-3岁', '4-6岁',
                                 '7-11岁', '12-17岁', '18-22岁', '23-30岁', '31-40岁', '41-49岁', '50-54岁', '55-59岁',
                                 '60-64岁', '65-69岁', '70-74岁', '75-79岁', '80岁以上']
        self.age_segment_count_list = []

    def test(self):
        df = pd.read_csv(self.age_segment_file)['投保范围_开始年龄结束年龄']
        # df.plot.bar( color='k', alpha=0.7)
        df1 = pd.read_csv(self.age_segment_file)
        age_range_sum = df.count()
        age_range_data_none = df[df.str.contains('无')].count()
        age_range_data_strange = df[df.str.contains('特殊数据')].count()

        # print(age_range_sum,age_range_data_strange)
        for i in range(self.age_segment_list.__len__()):
            age_segment = self.age_segment_list[i]
            count = df[df.str.contains(age_segment)].count()
            # print(count)
            self.age_segment_count_list.append(count)
        print(self.age_segment_count_list)
        df_charts = pd.DataFrame(self.age_segment_count_list, columns=['age_segment_count'], index=self.age_segment_list)
        print(df_charts)
        # sns.regplot(x=self.age_segment_list, y='Y轴 列名', hue='分组绘图参数', data=df)

        # sns.distplot(df, bins=None, hist=True, kde=False, rug=True, fit=None,
        #              hist_kws=None, kde_kws=None, rug_kws=None,
        #              fit_kws=None, color=None, vertical=False,
        #              norm_hist=False, axlabel=None, label=None, ax=None)

        # sns.distplot(df1['投保范围_开始年龄结束年龄'])
        # sns.barplot(x='day', y='total_bill', hue='sex', data=tips, order=None,
        #             hue_order=None, estimator=np.mean, ci=95,
        #             n_boot=1000, units=None, orient=None,
        #             color=None, palette=None, saturation=.75,
        #             errcolor=".26", errwidth=None, capsize=None,
        #             ax=None)
        # plt.show()


if __name__ == '__main__':
    charts_output = ChartsOutput()
    charts_output.test()
