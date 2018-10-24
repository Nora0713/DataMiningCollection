import pandas as pd
import ast
import re


class DataClean:
    def __init__(self):
        self.disease_raw = "../res/data/disease_edit.csv"
        self.medicare_raw = "../res/data/medicare_edit.csv"
        self.disease_once_clean = "../res/data/disease_cleaned_once.csv"
        self.medicare_once_clean = "../res/data/medicare_cleaned_once.csv"
        self.insurance_pregnancy = "../res/data/insurance_pregnancy.csv"
        self.disease_except_pregnancy = "../res/data/disease_except_pregnancy.csv"
        self.medicare_except_pregnancy = "../res/data/medicare_except_pregnancy.csv"
        self.disease_list = "../res/data/disease_list.txt"
        self.disease_cleaned_by_zn = "../res/data/disease_cleaned_by_zn.csv"
        self.correct_age_range_file = "../res/file/投保年龄更正.xlsx"
        self.correct_age_range_data = "../res/data/correct_age_range_data.csv"
        self.correct_age_range_data_twice = "../res/data/correct_age_range_data_twice.csv"
        # twice clean, correct some age-range data
        self.age_range_series_data = "../res/data/age_range_series_data.csv"
        self.count = 0
        self.age_segment_list = ['0岁', '1-7天', '8-15天', '16-27天', '28-30天', '31-50天', '50天-364天', '1-3岁', '4-6岁',
                                 '7-11岁', '12-17岁', '18-22岁', '23-30岁', '31-40岁', '41-49岁', '50-54岁', '55-59岁',
                                 '60-64岁', '65-69岁', '70-74岁', '75-79岁', '80岁以上']
        self.reg_age_range_list = [r'0岁(.)*', r'[1-7]日', r'([8-9]|(1[0-5]))日', r'((1[6-9])|(2[0-7]))日',
                                   r'(28|29|30)日',
                                   r'((3[1-9])|(4[0|9])|50)日',
                                   r'(([5-9][0-9])|([1-2][0-9][0-9])|(3([0-5][0-9])|(6[0-5])))日',
                                   r'[1-3]岁', r'[4-6]岁', r'([7-9]|(1[0-1]))岁', r'1[2-7]岁', r'((1[8-9])|(2[0-2]))岁',
                                   r'((2[3-9])|30)岁', r'((3[1-9])|40)岁', r'4[1-9]岁', r'5[0-4]岁', r'5[5-9]岁', r'6[0-4]岁',
                                   r'6[5-9]岁', r'7[0-4]岁', r'7[5-9]岁', '(([8-9][0-9])|(1[0-9][0-9]))岁']
        self.age_segment_file = "../res/data/age_segment_file.csv"
        self.disease_yiqing = "../res/data/disease_yiqing.csv"
        self.disease_set_package = "../res/data/disease_set_package.csv"

    def test(self):
        str = '{123恶性肿瘤bbbbbbbbb主动脉手术456}'
        pattern = re.compile('恶性肿瘤.*主动脉手术')
        res = re.search(pattern, str)
        print(str[0:res.start()] + '包1' + str[res.end():str.__len__()])

    def generate_insurance_pregnancy(self):
        df_disease_once_clean = pd.read_csv(self.disease_once_clean)
        df_medicare_once_clean = pd.read_csv(self.medicare_once_clean)

        df_disease_except_clean = df_disease_once_clean[
            ~df_disease_once_clean['投保范围_投保人符合条件集合'].str.contains('孕|妊娠|怀胎|分娩')]
        df_medicare_except_clean = df_medicare_once_clean[
            ~df_medicare_once_clean['投保范围_投保人符合条件集合'].str.contains('孕|妊娠|怀胎|分娩')]

        df_disease_except_clean.to_csv(self.disease_except_pregnancy)
        df_medicare_except_clean.to_csv(self.medicare_except_pregnancy)

    def package_disease_set(self):
        df_disease = pd.read_csv(self.disease_yiqing)
        df_package = df_disease[(df_disease['疾病的集合'].str.contains('恶性肿瘤')) &
                                # (df_disease['疾病的集合'].str.contains('急性心肌梗塞')) &
                                # (df_disease['疾病的集合'].str.contains('脑中风后遗症')) &
                                # (df_disease['疾病的集合'].str.contains('重大器官移植术或造血干细胞移植术')) &
                                # (df_disease['疾病的集合'].str.contains('冠状动脉搭桥术')) &
                                # (df_disease['疾病的集合'].str.contains('终末期肾病')) &
                                # (df_disease['疾病的集合'].str.contains('多个肢体缺失')) &
                                # (df_disease['疾病的集合'].str.contains('急性或亚急性重症肝炎')) &
                                # (df_disease['疾病的集合'].str.contains('良性脑肿瘤')) &
                                # (df_disease['疾病的集合'].str.contains('慢性肝功能衰竭失代偿期')) &
                                # (df_disease['疾病的集合'].str.contains('脑炎后遗症')) &
                                # (df_disease['疾病的集合'].str.contains('深度昏迷')) &
                                # (df_disease['疾病的集合'].str.contains('双耳失聪')) &
                                # (df_disease['疾病的集合'].str.contains('双目失明')) &
                                # (df_disease['疾病的集合'].str.contains('瘫痪')) &
                                # (df_disease['疾病的集合'].str.contains('心脏瓣膜手术')) &
                                # (df_disease['疾病的集合'].str.contains('严重阿尔茨海默病')) &
                                # (df_disease['疾病的集合'].str.contains('严重脑损伤')) &
                                # (df_disease['疾病的集合'].str.contains('严重帕金森病')) &
                                # (df_disease['疾病的集合'].str.contains('严重Ⅲ度烧伤')) &
                                # (df_disease['疾病的集合'].str.contains('严重原发性肺动脉高压')) &
                                # (df_disease['疾病的集合'].str.contains('严重运动神经元病')) &
                                # (df_disease['疾病的集合'].str.contains('语言能力丧失')) &
                                # (df_disease['疾病的集合'].str.contains('重型再生障碍性贫血')) &
                                (df_disease['疾病的集合'].str.contains('主动脉手术'))]
        # df_package['疾病的集合'].to_csv(self.disease_set_package)
        for index, row in df_disease.iterrows():
            disease_set = row['疾病的集合']
            pattern = re.compile('恶性肿瘤.*主动脉手术|主动脉手术.*恶性肿瘤')
            res = re.search(pattern, str(disease_set))
            if res is not None:
                value = disease_set[0:res.start()] + '包1' + disease_set[res.end():len(disease_set)]
                df_disease.loc[df_disease['filename'] == row['filename'], '疾病的集合'] = value
        df_disease['疾病的集合'].to_csv(self.disease_set_package)
        print(df_package.count())

    def get_disease_list(self):
        df_disease = pd.read_csv(self.disease_except_pregnancy)
        df_disease_set = df_disease['疾病的集合']
        disease_list = set()
        for disease_set in df_disease_set:
            for disease in ast.literal_eval(disease_set):
                disease_list.add(str(disease))
        print(len(disease_list))
        with open(self.disease_list, 'w', encoding='utf-8') as file:
            file.write(str(disease_list))

    def reg_sentence(self, string):
        # print(string)
        pattern = re.compile(r'.*{.*}.*|.*:.*')
        res = re.match(pattern, string)
        if res is not None:
            self.count += 1
        print(res)

    def clean_age_range(self):
        df_disease = pd.read_csv(self.correct_age_range_data_twice)
        for index, row in df_disease.iterrows():
            if row['投保范围_开始年龄结束年龄'] != '不详' and row['投保范围_开始年龄结束年龄'] != '无':
                age_range_array = ast.literal_eval(row['投保范围_开始年龄结束年龄'])
                if len(age_range_array) == 2:
                    start_age = age_range_array[0]
                    end_age = age_range_array[1]
                    # print(row['投保范围_开始年龄结束年龄'], self.reg_age_range(start_age), self.reg_age_range(end_age))
                    value = [start_age, end_age, self.reg_age_range(start_age), self.reg_age_range(end_age)]
                    print(str(value))
                    df_disease.loc[df_disease['filename'] == row['filename'], '投保范围_开始年龄结束年龄'] = str(value)
                else:
                    df_disease.loc[df_disease['filename'] == row['filename'], '投保范围_开始年龄结束年龄'] = '特殊数据' + row[
                        '投保范围_开始年龄结束年龄']
            else:
                df_disease.loc[df_disease['filename'] == row['filename'], '投保范围_开始年龄结束年龄'] = '无'
        df_disease.to_csv(self.age_segment_file)

    def reg_age_range(self, age):
        for i in range(self.reg_age_range_list.__len__()):
            reg_age = self.reg_age_range_list[i]
            pattern = re.compile(reg_age)
            res = re.match(pattern, age)
            if res is not None:
                # print(age[res.start():res.end()])
                return self.age_segment_list[i]


def correct_age_range(self):  # 投保年龄修改
    df_disease = pd.read_csv(self.disease_once_clean)
    df_correct_file = pd.read_excel(self.correct_age_range_file)
    for index, row in df_correct_file.iterrows():
        print(row['录入错误'], row['正确值'])
        df_disease.loc[df_disease['filename'] == row['录入错误'], '投保范围_开始年龄结束年龄'] = row['正确值']
    df_disease.to_csv(self.correct_age_range_data)


if __name__ == '__main__':
    data_clean = DataClean()
    data_clean.package_disease_set()
