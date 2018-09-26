import pandas as pd
import jieba
import jieba.analyse
from gensim import corpora, models
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块


# 分离5w和1w的数据

class WordCut:
    def __init__(self):
        self.data_5w_path = "../res/result/riskeys_ask_data_5w.csv"
        self.data_2k_path = "../res/result/riskeys_ask_data_2k.csv"
        self.stop_words_file = "../res/stopwords/stopwords.txt"
        self.output_file_2k = "../res/result/lda_riskeys_ask_data_result_2k.csv"
        self.output_file_5w = "../res/result/lda_riskeys_ask_data_result_5w.csv"

    def get_stop_words_set(self):
        with open(self.stop_words_file, mode='r', encoding='utf-8') as file:
            return set([line.strip() for line in file])

    def get_words_list(self, data):
        stop_words_set = self.get_stop_words_set()
        # print(stop_words_set)
        print("共计导入 %d 个停用词" % len(stop_words_set))
        word_list = []
        for line in data:
            tmp_list = list(jieba.cut(line.strip(), cut_all=False))
            word_list.append(
                [term for term in tmp_list if str(term) not in stop_words_set])  # 注意这里term是unicode类型，如果不转成str，判断会为假
        return word_list

    def lda(self, data, output_file):
        word_list = self.get_words_list(data)  # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
        word_dict = corpora.Dictionary(word_list)  # 生成文档的词典，每个词与一个整型索引值对应
        print(word_dict)
        corpus_list = [word_dict.doc2bow(text) for text in word_list]  # 词频统计，转化成空间向量格式
        print(corpus_list)
        lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=10, alpha='auto')
        print(lda.get_term_topics(100))
        with open(output_file, 'w', encoding='utf-8-sig') as f:
            for pattern in lda.show_topics():
                f.write(str(pattern))
                f.write('\n')


    def word_cloud(self):
        wordcloud  =  WordCloud(background_color="white").generate("")


if __name__ == '__main__':
    wc = WordCut()

    df_2k = pd.read_csv(wc.data_2k_path)
    list_2k = df_2k['ask'].tolist()
    wc.lda(list_2k, wc.output_file_2k)

    # df_5w = pd.read_csv(wc.data_5w_path)
    # list_5w = df_5w['ask'].tolist()
    # wc.lda(list_5w, wc.output_file_5w)
