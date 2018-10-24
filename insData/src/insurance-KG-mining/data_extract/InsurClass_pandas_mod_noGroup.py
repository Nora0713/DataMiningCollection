#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 20:17:08 2018

@author: qyin
"""
import pandas as pd

if __name__ == '__main__':
    #read data from excel
    df_life = pd.read_excel( 'InsurClass_pandas_mod.xlsx', 'lifeInsurance', index_col=None, na_values=['NA'])
    df_health = pd.read_excel( 'InsurClass_pandas_mod.xlsx', 'healthInsurance', index_col=None, na_values=['NA'])
    df_annuity = pd.read_excel( 'InsurClass_pandas_mod.xlsx', 'annuityInsurance', index_col=None, na_values=['NA'])
    df_accident = pd.read_excel( 'InsurClass_pandas_mod.xlsx', 'accidentInsurance', index_col=None, na_values=['NA'])
   
    #wipe group insurances from dataframe
    df_life_wipe = df_life[ df_life['产品名称'].str.contains("团体") == False ]
    df_health_wipe = df_health[ df_health['产品名称'].str.contains("团体") == False ]
    df_annuity_wipe = df_annuity[ df_annuity['产品名称'].str.contains("团体") == False ]
    df_accident_wipe = df_accident[ df_accident['产品名称'].str.contains("团体") == False ]
    
    writer = pd.ExcelWriter('InsurClass_pandas_mod_noGroup.xlsx')
    df_life_wipe.to_excel(writer, 'lifeInsurance_noGroup', index=False)
    df_health_wipe.to_excel(writer, 'healthInsurance_noGroup', index=False)
    df_annuity_wipe.to_excel(writer, 'annuityInsurance_noGroup', index=False)
    df_accident_wipe.to_excel(writer, 'accidentInsurance_noGroup', index=False)
    writer.save()