import json
import os
import csv

def get_files_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files
aim_dir=os.path.join(os.getcwd(),'label')
label_list=[]
for lable_fn in get_files_list(aim_dir):
    lable_f=open(os.path.join(aim_dir,lable_fn),'r',encoding='utf-8')
    l_j=json.load(lable_f)
    for l in l_j['label']:
        label_list.append(l)

# print(label_list)
def write_title():
    rst_file_name='first_output_result.csv'
    file=open(rst_file_name,'w')
    writer = csv.writer(file)
    l=[]
    l.append('filename')
    l.append('username')
    for l_j in label_list:
        l.append(l_j)
    writer.writerow(l)

filename_content_dict={}

def filename_content_mapping():
    aim_dir='filename_txt_mapping'
    mapping_filename=os.path.join(os.getcwd(),aim_dir)
    for filename in get_files_list(mapping_filename):
        file=open(os.path.join(mapping_filename,filename))
        rst_j=json.load(file)
        for l in rst_j:
            filename_content_dict[l['content']]=l['file_name']

filename_content_mapping()
final_dict={}

def handle_single_output():
    aim_dir='first_output'
    dir=os.path.join(os.getcwd(),aim_dir)
    cnt = 0

    for filename in get_files_list(dir):

        idx=filename.find('task')
        username=filename[:idx]
        if username not in final_dict:
            final_dict[username]={}

        idx_point=filename.find('.')
        # print(filename[idx:idx_point])
        file=open(os.path.join(dir,filename),'r')
        rst_j = json.load(file)
        for l in rst_j['result']:
            if l['content'] not in filename_content_dict:
                cnt+=1
                mapping_txt_filename='filename'+str(cnt)
                if mapping_txt_filename not in final_dict[username]:
                    final_dict[username][mapping_txt_filename] = {}
                    task_num=0
                    for label in label_list:
                        if label=='其他':
                            task_num+=1
                        if (label=='其他' or label =='数据条件') and task_num >=1:
                            final_dict[username][mapping_txt_filename][label+str(task_num)] = []
                        else:
                            final_dict[username][mapping_txt_filename][label]=[]
                for span in l['spans']:
                    if span['label'] == '其他' or  span['label']== '数据条件':
                        if idx_point =='task1' or idx_point =='task4' or idx_point =='task7':
                            final_dict[username][mapping_txt_filename][span['label']+str(1)] .append(span['span_name'])
                        if idx_point =='task2' or idx_point =='task5' or idx_point =='task8':
                            final_dict[username][mapping_txt_filename][span['label']+str(2)].append(span['span_name'])
                        if idx_point == 'task3' or idx_point == 'task6' or idx_point == 'task9':
                            final_dict[username][mapping_txt_filename][span['label'] +str(3)] .append(span['span_name'])
                    else:
                        final_dict[username][mapping_txt_filename][span['label']].append(span['span_name'])
            else:
                mapping_txt_filename = filename_content_dict[l['content']]
                if mapping_txt_filename not in final_dict[username]:
                    final_dict[username][mapping_txt_filename] = {}
                    task_num = 0
                    for label in label_list:
                        if label=='其他':
                            task_num+=1
                        if (label=='其他' or label =='数据条件') and task_num >=1:
                            final_dict[username][mapping_txt_filename][label+str(task_num)] = []
                        else:
                            final_dict[username][mapping_txt_filename][label]=[]
                for span in l['spans']:
                    if span['label'] == '其他' or span['label'] == '数据条件':
                        if idx_point =='task1' or idx_point =='task4' or idx_point =='task7':
                            final_dict[username][mapping_txt_filename][span['label']+str(1)] .append(span['span_name'])
                        if idx_point =='task2' or idx_point =='task5' or idx_point =='task8':
                            final_dict[username][mapping_txt_filename][span['label']+str(2)] .append(span['span_name'])
                        if idx_point == 'task3' or idx_point == 'task6' or idx_point == 'task9':
                            final_dict[username][mapping_txt_filename][span['label'] +str(3)] .append(span['span_name'])
                    else:
                        final_dict[username][mapping_txt_filename][span['label']].append(span['span_name'])

handle_single_output()

def write_left_columns():
    rst_file_name = 'first_output_result.csv'
    file = open(rst_file_name, 'w',encoding='utf-8')
    writer = csv.writer(file)
    l = []
    l.append('filename')
    l.append('username')
    for l_j in label_list:
        l.append(l_j)
    writer.writerow(l)
    for username in final_dict.keys():
        for filename in final_dict[username].keys():
            l=[]
            l.append(filename)
            l.append(username)
            for v in final_dict[username][filename].values():
                if v == []:
                    l.append('无')
                else:
                    l.append(v)
            writer.writerow(l)

write_left_columns()