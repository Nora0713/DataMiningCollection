import pikepdf
from urllib import parse, request
import re
import docx

test_docx_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/testdata/0a0f2c3d-9e2e-4da6-8513-134906c96011_TERMS.docx'
test_txt_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/ae1715f2-eed6-4be9-9ce9-0c5c6d70d951_TERMS.PDF.txt'
file_list_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/0_files_list.txt'
count = 0


def read_docx(docx_path):
    doc = docx.Document(docx_path)
    wholedoc = ""
    for para in doc.paragraphs:
        wholedoc += para.text
        wholedoc += '\n'
    print(wholedoc)
    return wholedoc


def get_age_para(s, filename):
    # f = open(test_txt_path, "r", encoding='utf-8')
    save = open('test.txt', 'a+', encoding='utf-8')
    # s = f.read()
    try:
        pattern = "\d([.]\d)+\s+(投保范围|年龄)\s+[\u4e00-\u9fa5]+\s*"
        match = re.search(pattern, s, re.M)
        begin = match.start()
        start = match.end()
        match1 = re.search("\d[.]\d*\s+[\u4e00-\u9fa5]+", s[start:], re.M)
        end = match1.start()
        print(s[begin:end + start], file=save)
        print('====================\n', file=save)
    except:
        try:
            pattern = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+(投保范围|年龄)(\n|\s)+[\u4e00-\u9fa5]+\s*"
            pattern_sub = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+"
            match = re.search(pattern, s, re.M)
            begin = match.start()
            start = match.end()
            match1 = re.search(pattern_sub, s[start:], re.M)
            end = match1.start()
            print(s[begin:end + start], file=save)
            print('====================\n', file=save)
        except:
            print(filename + 'Error', file=save)
            global count
            count = count + 1
            pass
        # print(filename + 'Error', file=save)
        # global count
        # count = count + 1
        # pass


def test_age_para():
    file_list = open(file_list_path, "r", encoding='utf-8').readlines()
    for filename in file_list:
        txt_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/' + filename.strip() + '.txt'
        s = open(txt_path, "r", encoding='utf-8').read()
        get_age_para(s, filename)
    print(count)


test_age_para()