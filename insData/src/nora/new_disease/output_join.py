import util
import os
import json
have_used_file_list=[]

dir_dict={'result':[]}
dir=os.path.join(os.getcwd(),'first_output')
# filename_content_dict=util.get_filename_content_dict()

for f in util.get_files_list(dir):
    filename=os.path.join(dir,f)
    file=open(filename,'r')
    rst_j=json.load(file)
    for l in rst_j['result']:
        already_in_there=False
        for data in dir_dict['result']:
            if data['data_id']==l['data_id']:
                data['spans']=data['spans']+l['spans']
                already_in_there=True
        if not already_in_there:
            dir_dict['result'].append(l)
//加入300疾病
dir=os.path.join(os.getcwd(),'add_new_300_disease_label')
for f in util.get_files_list(dir):
    filename=os.path.join(dir,f)
    file=open(filename,'r')
    rst_j=json.load(file)
    for l in rst_j['result']:
        already_in_there=False
        for data in dir_dict['result']:
            if data['data_id']==l['data_id']:
                data['spans']=data['spans']+l['spans']
                already_in_there=True
        if not already_in_there:
            dir_dict['result'].append(l)
//去掉wxy的10个
dir=os.path.join(os.getcwd(),'tmp_dir')
for f in util.get_files_list(dir):
    filename=os.path.join(dir,f)
    file=open(filename,'r')
    rst_j=json.load(file)
    for l in rst_j['result']:
        for data in dir_dict['result']:
            if data['content']==l['content']:
                data['spans']=l['spans']
                print('1')
//重排序
for data in dir_dict['result']:
    data['spans']=sorted(data['spans'], key=lambda e: e.__getitem__('label'))



jsonObj = json.dumps(dir_dict, ensure_ascii=False)
fileJson = open('all_output.json', 'w', encoding='utf-8')
fileJson.write(jsonObj)
fileJson.close()
