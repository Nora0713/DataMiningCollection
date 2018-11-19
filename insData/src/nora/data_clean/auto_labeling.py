import requests
import json


def age():
    requrl = "http://tryraptor.mlamp.cn/services/nora/397"
    params = {"content": "jdfhdkjhgsdjfghdsjkfg"}
    result = requests.post(url=requrl, json=params).text
    print(result)


# 保险责任的选择
def insurance_duty():
    with open('/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean/test1109.json',
              encoding='utf-8-sig') as j:
        lines = j.readlines()
        json_raw_string = ""
        for line in lines:
            json_raw_string = json_raw_string + line
        data = json.loads(json_raw_string)
        content = data['result'][0]['content']
        print(content)
        requrl = "http://tryraptor.mlamp.cn/services/nora/397"
        params = {"content": content}
        result = requests.post(url=requrl, json=params).text
        print(result)


age()
