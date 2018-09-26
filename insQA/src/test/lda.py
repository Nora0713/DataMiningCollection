import os
import jieba
from openpyxl import load_workbook
import jieba.analyse
from gensim import corpora, models
import numpy as np

raw_data_file_path_6w = os.getcwd() + "/res/riskeys_records_ask.xlsx"
raw_data_file_6w_sheet = "riskeys-back_records_ask"
raw_data_file_path = os.getcwd() + "/res/riskey_data_100.xlsx"
raw_data_file_sheet = "Sheet1"
stop_words_file_name = os.getcwd() + "/res/stopwords/stop_words_zh.txt"
cleaned_data = os.getcwd() + "/res/clean_data"
output_file = os.getcwd() + "/res/lda_output.txt"


def clean_data(path, sheet):
    riskeys_ask_data = load_workbook(path)[sheet]
    riskeys_ask_list = ['怎么买保险', 'kaolv考虑']
    for cell in list(riskeys_ask_data.columns)[3]:
        riskeys_ask_list.append(cell.value)
    write_list(riskeys_ask_list)
    return riskeys_ask_list


def write_list(data):
    with open(os.getcwd() + "/res/clean_data", mode='w', encoding='utf-8-sig') as f:
        for item in data:
            if len(str(item).strip()) != 0:
                f.write(str(item).replace('\n', ''))
                f.write('\n')
        # line.encode('utf-8').decode('unicode_escape')


def get_stop_words_set(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        return set([line.strip() for line in file])


def get_words_list(file_name, stop_word_file_name):
    stop_words_set = get_stop_words_set(stop_word_file_name)
    print(stop_words_set)
    print("共计导入 %d 个停用词" % len(stop_words_set))
    word_list = []
    with open(file_name, mode='r', encoding='utf-8-sig') as file:
        for line in file:
            tmp_list = list(jieba.cut(line.strip(), cut_all=False))
            word_list.append(
                [term for term in tmp_list if str(term) not in stop_words_set])  # 注意这里term是unicode类型，如果不转成str，判断会为假
    return word_list


def lda():
    raw_msg_file_name = cleaned_data
    stop_word_file_name = stop_words_file_name
    word_list = get_words_list(raw_msg_file_name, stop_word_file_name)  # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
    word_dict = corpora.Dictionary(word_list)  # 生成文档的词典，每个词与一个整型索引值对应
    corpus_list = [word_dict.doc2bow(text) for text in word_list]  # 词频统计，转化成空间向量格式
    lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=10, alpha='auto')
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        for pattern in lda.show_topics():
            f.write(str(pattern))
            f.write('\n')


if __name__ == '__main__':
    clean_data(raw_data_file_path_6w, raw_data_file_6w_sheet)
