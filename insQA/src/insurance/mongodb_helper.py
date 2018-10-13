from pymongo import MongoClient


class DbHelper:
    def conn_db(self):
        client = MongoClient('118.89.234.98',27017)
        insuance_db = client.insurance