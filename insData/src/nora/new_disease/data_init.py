import pikepdf
from urllib import parse, request
import json
import docx
import os
import shutil

new_disease_serious_json_file = "/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/new_disease_serious.json"
new_available_file = "/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/new_available_file.txt"


def download_new_disease_pdf_files():
    # pdf = pikepdf.open('input.pdf')
    # num_pages = len(pdf.pages)
    # del pdf.pages[-1]
    # pdf.save('output.pdf')

    with open(new_disease_serious_json_file, encoding='utf-8-sig') as j:
        lines = j.readlines()
        json_raw_string = ""
        for line in lines:
            json_raw_string = json_raw_string + line
        data = json.loads(json_raw_string)
        for item in data:
            url = item['PDF文件']
            pdf_name = url[32:]
            print(pdf_name)
            response = request.urlopen(url)  # .read()#.decode('utf-8')
            pdf = pikepdf.open(response)
            num_pages = len(pdf.pages)
            # del pdf.pages[-1]
            pdf.save(
                '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/out_of_date_new_disease_raw_docx/' + pdf_name)


def read_word():
    test_word_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/out_of_date_new_disease_raw_docx/0a0f2c3d-9e2e-4da6-8513-134906c96011_TERMS.docx'
    doc = docx.Document(test_word_path)
    wholedoc = ""
    for para in doc.paragraphs:
        wholedoc += para.text
        wholedoc += '\n'
    print(wholedoc)


def test_complete_converted():
    with open(new_disease_serious_json_file, encoding='utf-8-sig') as j:
        lines = j.readlines()
        json_raw_string = ""
        for line in lines:
            json_raw_string = json_raw_string + line
        data = json.loads(json_raw_string)
        count = 0
        for item in data:
            url = item['PDF文件']
            pdf_name = url[32:-4]
            word_name = pdf_name + '.docx'
            # print(word_name)
            path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/out_of_date_new_disease_raw_docx/' + word_name
            try:
                f = open(path)
                f.close()
            except IOError:
                count += 1
                print(word_name + " File is not accessible.")
        print(str(count) + ' files are not accessible.')


def get_available_insurance():
    with open(new_disease_serious_json_file, encoding='utf-8-sig') as j:
        save_file = open(new_available_file, 'a+')
        lines = j.readlines()
        json_raw_string = ""
        for line in lines:
            json_raw_string = json_raw_string + line
        data = json.loads(json_raw_string)
        status_dict = {}
        for item in data:
            url = item['PDF文件']
            pdf_name = url[32:]
            print(pdf_name)
            status = item['产品销售状态']
            # if status == '在售':
            #     print(pdf_name, file=save_file)
            if status not in status_dict:
                status_dict[status] = 0
            else:
                status_dict[status] += 1
        print(status_dict)


def clean_out_of_date_insurance():
    dir_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/out_of_date_new_disease_raw_docx/'
    out_of_date_path = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/new_disease_raw_docx/'
    dir = os.listdir(dir_path)
    print(dir)
    available_file_list = open(new_available_file, 'r').readlines()
    # for line in available_file_list:
    #     filename = line.strip()[:-4] + '.docx'
    #     print(filename)
    #     if os.path.exists(dir_path + filename):
    #         shutil.move(dir_path + filename, out_of_date_path + filename)
    for line in available_file_list:
        filename = line.strip()[:-4] + '.docx'
        print(filename)
        if os.path.exists(dir_path + filename):
            print(1)

if __name__ == '__main__':
    get_available_insurance()
