from pymongo import MongoClient
from urllib import parse, request
import re


class DbHelper:
    def __init__(self):
        self.user = parse.quote_plus('inskg')
        self.passeord = parse.quote_plus('kg2018')

    def test(self):
        a = 1

    def get_edited_disease_filename_list(self):
        client = MongoClient('mongodb://118.89.234.98:27017')
        db = client.insurance
        db.authenticate(self.user, self.passeord)
        disease_edit = db.disease_edit
        mquery = {}
        cursor_disease_edit = disease_edit.find(mquery)
        print(cursor_disease_edit.count())
        filename_list = []
        for disease_edit_item in cursor_disease_edit:
            filename_list.append(disease_edit_item['filename'])
        return filename_list

    def download_txt_file(self, filename_list):
        not_found_count = 0
        for file_name in filename_list:
            txt_url = 'http://118.89.234.98/insurance_get_ext_result/attr_get_' + file_name + '.txt'
            write_txt = '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/' + file_name + '.txt'
            not_found_file = open(
                '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/0_not_found_file.txt',
                'a+', encoding='utf-8')
            files_list = open(
                '/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data/old_disease_raw_txt/0_files_list.txt',
                'a+', encoding='utf-8')
            try:
                f = open(write_txt)
                f.close()
                print(file_name, file=files_list)
            except IOError:
                try:
                    response = request.urlopen(txt_url)  # .read()#.decode('utf-8')
                    with open(write_txt, "wb") as code:
                        code.write(response.read())
                    print(file_name, file=files_list)
                except:
                    not_found_count += 1
                    print(file_name, file=not_found_file)
        print(not_found_count, file=not_found_file)


if __name__ == '__main__':
    dbhelper = DbHelper()
    list = dbhelper.get_edited_disease_filename_list()
    print(list)
    # dbhelper.download_txt_file(list)
