import json

raw_disease_json = "/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean_2/disease_set/disease_1205.json"
output_file = "/Users/zhaoning/Documents/project/dataMining/userIntent/insData/src/nora/data_clean_2/disease_set/output.txt"


def stat_disease():
    j = open(raw_disease_json, encoding='utf-8-sig')
    save_file = open(output_file, 'a+')
    lines = j.readlines()
    json_raw_string = ""
    for line in lines:
        json_raw_string = json_raw_string + line
    data = json.loads(json_raw_string)
    data_result = data['results']

    disease_dict = {}
    for result in data_result:
        disease_data_item = result['result']
        if len(disease_data_item) > 0:
            disease_collection = disease_data_item[0]['疾病组别']
            if len(disease_collection) > 0:
                disease_set_item = disease_collection[0]['疾病']
                for item in disease_set_item:
                    disease_name = str(item['疾病名称'])
                    print(disease_name)
                    disease_name = disease_name.strip()
                    print(disease_name)
                    disease_dict[disease_name] = 0 if disease_name not in disease_dict else disease_dict[
                                                                                                disease_name] + 1
    for item in disease_dict:
        print(item, file=save_file)


stat_disease()
