from pymongo import MongoClient


class DbHelper:
    def conn_db:
        client = MongoClient('118.89.234.98',27017)
        insuance_db = client.insurance
        collection =