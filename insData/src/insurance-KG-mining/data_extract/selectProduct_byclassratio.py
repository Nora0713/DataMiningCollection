#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:39:40 2018

@author: qyin
"""

import pandas as pd
import random
from shutil import copyfile
import math

#input df:dataframe ; category:column index ; name:category value ;ratio: choose proportion from all
#output product links as list
def selectProduct(df, category , name, ratio):
    #filter data and then reset index from 0
    df_filter = df[df[category] == name].reset_index(drop = True)
    number = len(df_filter)
    choose_number = math.ceil(number*ratio)
    
    if choose_number >= 10:
        final = choose_number
    elif number >= 10:
        final = 10
    else:
        final = number
            
            
    index_sample = random.sample(range(len(df_filter)), k = final)
    #s1.iloc(0) _iLocIndexer is callable 
    #s1.iloc[0] is called with square brackets, an _iLocIndexer is instantiated and the call to [] operator results in a call to the iLocIndexer's `getitem' method.
    #choose_products = df_filter.iloc(index_sample) #is modified , reason given above
    choose_products = df_filter.iloc[index_sample]
    #print(type(choose_products)) #<pandas.core.indexing._iLocIndexer at 0x11c188cc0>
    
    #return dataframe
    return choose_products  #['说明书链接'].tolist()

#input links list
#output names list
def link_to_name(links):
    choose_names = list()
    for url in links:
        index = url.rfind('/',0,len(url))
        file_name = url[index+1:]
        choose_names.append(file_name)
    return choose_names 

def copyfiles(bigclass, smallclass, names):
    path_s = 'insurances_byid_qpdf/'
    path_d = 'selectProducts_num200/'+bigclass+'_'+smallclass+'/'
    for n in names:
        copyfile(path_s+n, path_d+n)
    
    
if __name__ == '__main__':
    #read data from excel
    df_life = pd.read_excel( 'InsurClass_pandas_mod_noGroup.xlsx', 'lifeInsurance_noGroup', index_col=None, na_values=['NA'])
    df_health = pd.read_excel( 'InsurClass_pandas_mod_noGroup.xlsx', 'healthInsurance_noGroup', index_col=None, na_values=['NA'])
    df_annuity = pd.read_excel( 'InsurClass_pandas_mod_noGroup.xlsx', 'annuityInsurance_noGroup', index_col=None, na_values=['NA'])
    df_accident = pd.read_excel( 'InsurClass_pandas_mod_noGroup.xlsx', 'accidentInsurance_noGroup', index_col=None, na_values=['NA'])
    
    totalNum = len(df_life) + len(df_health) + len(df_annuity) + len(df_accident) 

     #choose products ratio ; in order to select 200 pdfs in total
    ratio = 200/float(totalNum)
    #for life
    life_regular = selectProduct(df_life , '类别2', '定期寿险', ratio)
    life_both = selectProduct(df_life , '类别2', '两全寿险', ratio)
    life_whole = selectProduct(df_life , '类别2', '终身寿险', ratio)
    total_life = len(life_regular)+len(life_both)+len(life_whole)
     
    select_life_regular = link_to_name(life_regular['说明书链接'].tolist()) 
    select_life_both = link_to_name(life_both['说明书链接'].tolist())
    select_life_whole = link_to_name(life_whole['说明书链接'].tolist())
    #for health
    health_nurse = selectProduct(df_health, '类别3', '护理保险', ratio)
    health_disease = selectProduct(df_health, '类别3', '疾病保险', ratio)
    health_disability = selectProduct(df_health, '类别3', '失能收入损失保险', ratio)
    health_medical = selectProduct(df_health, '类别3', '医疗保险', ratio)
    total_health = len(health_nurse) + len(health_disease)+len(health_disability)+len(health_medical)
    
    select_health_nurse = link_to_name(health_nurse['说明书链接'].tolist())
    select_health_disease = link_to_name(health_disease['说明书链接'].tolist())
    select_health_disability = link_to_name(health_disability['说明书链接'].tolist())
    select_health_medical = link_to_name(health_medical['说明书链接'].tolist())
    #for annuity
    annuity_aged = selectProduct(df_annuity , '类别2', '养老年金保险', ratio)
    annuity_non = selectProduct(df_annuity , '类别2', '非养老年金保险', ratio)
    total_annuity = len(annuity_aged)+len(annuity_non)
    
    select_annuity_aged = link_to_name(annuity_aged['说明书链接'].tolist())
    select_annuity_non = link_to_name(annuity_non['说明书链接'].tolist())
    #for accident
    accident = selectProduct(df_accident , '类别1', '意外伤害保险', ratio)
    total_accident = len(accident)
    
    select_accident = link_to_name(accident['说明书链接'].tolist())
    
    #copy files
    #for life
    copyfiles('人寿保险','定期寿险', select_life_regular) #人寿保险_定期寿险
    copyfiles('人寿保险','两全寿险', select_life_both)#人寿保险_两全寿险
    copyfiles('人寿保险','终身寿险', select_life_whole)#人寿保险_终身寿险
    #for health
    copyfiles('健康保险','护理保险', select_health_nurse)#健康保险_护理保险
    copyfiles('健康保险','疾病保险', select_health_disease)#健康保险_疾病保险
    copyfiles('健康保险','失能收入损失保险', select_health_disability)#健康保险_失能收入损失保险
    copyfiles('健康保险','医疗保险', select_health_medical)#健康保险_医疗保险
    
    copyfiles('年金保险','养老年金保险', select_annuity_aged)#年金保险_养老年金保险
    copyfiles('年金保险','非养老年金保险', select_annuity_non)#年金保险_非养老年金保险
    
    copyfiles('意外伤害保险','', select_accident)#意外伤害保险_
    
    with open(r'selectProducts_num200/description.txt','a', encoding = 'utf-8') as f:
        total = total_life + total_health + total_annuity + total_accident
        f.write("总抽取数 : "+ str(total) + '\n')
        f.write("人寿保险数 : "+ str(total_life) + '\n')
        f.write("人寿保险_定期寿险数 : "+ str(len(life_regular)) + '\n')
        life_regular.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("人寿保险_两全寿险数 : "+ str(len(life_both)) + '\n')
        life_both.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("人寿保险_终身寿险数 : "+ str(len(life_whole)) + '\n')
        life_whole.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        #len(health_nurse) + len(health_disease)+len(health_disability)+len(health_medical)
        f.write("健康保险数 : "+ str(total_health) + '\n')
        f.write("健康保险_护理保险 : "+ str(len(health_nurse)) + '\n')
        health_nurse.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("健康保险_疾病保险 : "+ str(len(health_disease)) + '\n')
        health_disease.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("健康保险_失能收入损失保险 : "+ str(len(health_disability)) + '\n')
        health_disability.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("健康保险_医疗保险 : "+ str(len(health_medical)) + '\n')
        health_medical.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        
        f.write("年金保险数 : "+ str(total_annuity) + '\n')
        f.write("年金保险_养老年金保险 : "+ str(len(annuity_aged)) + '\n')
        annuity_aged.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        f.write("年金保险_非养老年金保险 : "+ str(len(annuity_non)) + '\n')
        annuity_non.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
        
        f.write("意外伤害保险_ : "+ str(total_accident) + '\n')
        accident.to_csv(r'selectProducts_num200/description.txt', index=None, sep=' ', mode='a')
     
        
    

    
    
    
    
    