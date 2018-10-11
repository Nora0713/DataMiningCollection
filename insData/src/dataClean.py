import pandas as pd
import ast


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

    def test(self):
        df_disease_raw = pd.read_csv(self.disease_raw)
        df_disease_set = df_disease_raw[(df_disease_raw['疾病的集合'].str.contains(r'(*)'))]
        print(df_disease_set.count())

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
        df_disease = pd.read_csv(self.disease_except_pregnancy)
        df_package = df_disease[(df_disease['疾病的集合'].str.contains('恶性肿瘤')) &
                                (df_disease['疾病的集合'].str.contains('急性心肌梗塞')) &
                                (df_disease['疾病的集合'].str.contains('脑中风后遗症')) &
                                (df_disease['疾病的集合'].str.contains('重大器官移植术或造血干细胞移植术')) &
                                (df_disease['疾病的集合'].str.contains('冠状动脉搭桥术')) &
                                (df_disease['疾病的集合'].str.contains('终末期肾病')) &
                                (df_disease['疾病的集合'].str.contains('多个肢体缺失')) &
                                (df_disease['疾病的集合'].str.contains('急性或亚急性重症肝炎')) &
                                (df_disease['疾病的集合'].str.contains('良性脑肿瘤')) &
                                (df_disease['疾病的集合'].str.contains('慢性肝功能衰竭失代偿期')) &
                                (df_disease['疾病的集合'].str.contains('脑炎后遗症')) &
                                (df_disease['疾病的集合'].str.contains('深度昏迷')) &
                                (df_disease['疾病的集合'].str.contains('双耳失聪')) &
                                (df_disease['疾病的集合'].str.contains('双目失明')) &
                                (df_disease['疾病的集合'].str.contains('瘫痪')) &
                                (df_disease['疾病的集合'].str.contains('心脏瓣膜手术')) &
                                (df_disease['疾病的集合'].str.contains('严重阿尔茨海默病')) &
                                (df_disease['疾病的集合'].str.contains('严重脑损伤')) &
                                (df_disease['疾病的集合'].str.contains('严重帕金森病')) &
                                (df_disease['疾病的集合'].str.contains('严重Ⅲ度烧伤')) &
                                (df_disease['疾病的集合'].str.contains('严重原发性肺动脉高压')) &
                                (df_disease['疾病的集合'].str.contains('严重运动神经元病')) &
                                (df_disease['疾病的集合'].str.contains('语言能力丧失')) &
                                (df_disease['疾病的集合'].str.contains('重型再生障碍性贫血')) &
                                (df_disease['疾病的集合'].str.contains('主动脉手术'))]
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


if __name__ == '__main__':
    data_clean = DataClean()
    data_clean.test()
