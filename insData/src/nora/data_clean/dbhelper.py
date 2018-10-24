from pymongo import MongoClient
import urllib.parse
import re


class DbHelper:
    def __init__(self):
        self.user = urllib.parse.quote_plus('inskg')
        self.passeord = urllib.parse.quote_plus('kg2018')

    def test(self):
        a = 1

    def init_insurance_contain_yun(self):
        client = MongoClient('mongodb://118.89.234.98:27017')
        db = client.insurance
        db.authenticate(self.user, self.passeord)
        col_disease_edit = db.disease_edit
        col_medicare_edit = db.medicare_edit
        mquery = {"$or": [{"投保范围.投保人符合条件集合": re.compile('孕')}, {"投保范围.投保人符合条件集合": re.compile('妊娠')}]}
        # cursor_disease_contain_yun = col_disease_edit.find(mquery)
        cursor_medicare_contain_yun = col_medicare_edit.find(mquery)
        print(cursor_medicare_contain_yun.count())

        col_insurance_contain_yun = db.insurance_contain_yun
        col_insurance_contain_yun.insert_many(list(cursor_medicare_contain_yun))

    def delete_insurance_contain_yun(self):
        client = MongoClient('mongodb://118.89.234.98:27017')
        db = client.insurance
        db.authenticate(self.user, self.passeord)
        col_disease_edit = db.disease_edit
        col_medicare_edit = db.medicare_edit
        mquery = {
            "$and": [{"投保范围.投保人符合条件集合": {'$not': re.compile('孕')}}, {"投保范围.投保人符合条件集合": {'$not': re.compile('妊娠')}}]}
        cursor_disease_not_contain_yun = col_disease_edit.find(mquery)
        cursor_medicare_not_contain_yun = col_medicare_edit.find(mquery)
        print(cursor_disease_not_contain_yun.count())
        print(cursor_medicare_not_contain_yun.count())

        col_disease_except_yun = db.disease_except_yun
        col_disease_except_yun.insert_many(list(cursor_disease_not_contain_yun))

        col_medicare_except_yun = db.medicare_except_yun
        col_medicare_except_yun.insert_many(list(cursor_medicare_not_contain_yun))


if __name__ == '__main__':
    dbhelper = DbHelper()
    dbhelper.delete_insurance_contain_yun()
