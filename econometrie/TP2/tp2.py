import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_stata('/Users/gabrielderome/Desktop/tp/econometrie/TP2/data_angrist_evans.dta')
print(df.columns)

df['married'] = df['marst'] != 6
#if the values of married == True then change the value to 1 else 0
df['married'] = df['married'].astype(int)
#if value in nchild is == 9+ then change the value to 9
df['nchild'] = df['nchild'].replace('9+', '9')
#convert nchild to int
df['nchild'] = df['nchild'].astype(int)
#create column for more than 2 children
df['morethantwo'] = df['nchild'] > 2
#convert column to int
df['morethantwo'] = df['morethantwo'].astype(int)
#remove NaN values
df['firstborn_male'] = df['firstborn_male'].fillna(0)
df['secondborn_male'] = df['secondborn_male'].fillna(0)
df['firstborn_fem'] = df['firstborn_fem'].fillna(0)
df['secondborn_fem'] = df['secondborn_fem'].fillna(0)

#create column "twoboys" where True if firsborn_male and secondborn_male != 0
df['twoboys'] = (df['firstborn_male'] != 0) | (df['secondborn_male'] != 0)
df['twogirls'] = (df['firstborn_fem'] != 0) | (df['secondborn_fem'] != 0)
#create samesex column where True if twoboys or twogirls == True
df['samesex'] = (df['twoboys'] == True) | (df['twogirls'] == True)

#convert twoboys, twogirls and samesex to int
df['twoboys'] = df['twoboys'].astype(int)
df['twogirls'] = df['twogirls'].astype(int)
df['samesex'] = df['samesex'].astype(int)


df['eldch'] = df['eldch'].replace('Less than 1 year old', '1')
df['yngch'] = df['yngch'].replace('Less than 1 year old', '1')

#convert eldch to int
df['eldch'] = df['eldch'].astype(int)
df['yngch'] = df['yngch'].astype(int)

#create column twins where True if eldch == yngch
df['twins'] = df['eldch'] == df['yngch']
#convert twins and age to int
df['twins'] = df['twins'].astype(int)
df['age'] = df['age'].astype(int)

#create new column agefirst where age - eldch
df['agefirst'] = df['age'] - df['eldch']

#if the value starts with 'N' then change the value to 0 else 1
df['labforce'] = df['labforce'].str.startswith('N').astype(int)

#change the value to 0 if 'N/A'
df['wkswork2'] = df['wkswork2'].replace('N/A', '0')
#change the value of the categories to be the mean between the two values
df['wkswork2'] = df['wkswork2'].replace('1-13 weeks', '7')
df['wkswork2'] = df['wkswork2'].replace('14-26 weeks', '20')
df['wkswork2'] = df['wkswork2'].replace('27-39 weeks', '33')
df['wkswork2'] = df['wkswork2'].replace('40-47 weeks', '44')
df['wkswork2'] = df['wkswork2'].replace('48-49 weeks', '48.5')
df['wkswork2'] = df['wkswork2'].replace('50-52 weeks', '51')

df['wkswork2'] = df['wkswork2'].astype('string').astype('float')





#change the value to 0 if 'N/A'
df['hrswork2'] = df['hrswork2'].replace('N/A', '0')
#change the value of the categories to be the mean between the two values
df['hrswork2'] = df['hrswork2'].replace('1-14 hours', '7.5')
df['hrswork2'] = df['hrswork2'].replace('15-29 hours', '22')
df['hrswork2'] = df['hrswork2'].replace('30-34 hours', '32')
df['hrswork2'] = df['hrswork2'].replace('35-39 hours', '37')
df['hrswork2'] = df['hrswork2'].replace('40 hours', '40')
df['hrswork2'] = df['hrswork2'].replace('41-48 hours', '44.5')
df['hrswork2'] = df['hrswork2'].replace('49-59 hours', '54')
df['hrswork2'] = df['hrswork2'].replace('60+ hours', '60')
df['hrswork2'] = df['hrswork2'].astype('string').astype('float')

#print all values from labforce
print(df['inctot'].value_counts())
print(df['ftotinc'].value_counts())

#create new column where ftotinc - inctot
df['nonwifeinc'] = df['ftotinc'] - df['inctot']


#create df where only sex == 'Female'
female = df.loc[df['sex'] == 'Female']
married_female = df.loc[df['married'] == 1]
married_male = df.loc[(df['sex'] == 'Male') & (df['married'] == 1)]

#get the number of rows in each df
female_rows = female.shape[0]
married_female_rows = married_female.shape[0]
married_male_rows = married_male.shape[0]

#get the means and std
mean_nchild_w_all = female['nchild'].mean()
std_nchild_w_all = female['nchild'].std()
mean_nchild_w_married = married_female['nchild'].mean()
std_nchild_w_married = married_female['nchild'].std()

mean_mt2_w_all = female['morethantwo'].mean()
std_mt2_w_all = female['morethantwo'].std()
mean_mt2_w_married = married_female['morethantwo'].mean()
std_mt2_w_married = married_female['morethantwo'].std()

mean_fbm_w_all = female['firstborn_male'].mean()
std_fbm_w_all = female['firstborn_male'].std()
mean_fbm_w_married = married_female['firstborn_male'].mean()
std_fbm_w_married = married_female['firstborn_male'].std()

mean_sbm_w_all = female['secondborn_male'].mean()
std_sbm_w_all = female['secondborn_male'].std()
mean_sbm_w_married = married_female['secondborn_male'].mean()
std_sbm_w_married = married_female['secondborn_male'].std()

mean_tb_w_all = female['twoboys'].mean()
std_tb_w_all = female['twoboys'].std()
mean_tb_w_married = married_female['twoboys'].mean()
std_tb_w_married = married_female['twoboys'].std()

mean_tg_w_all = female['twogirls'].mean()
std_tg_w_all = female['twogirls'].std()
mean_tg_w_married = married_female['twogirls'].mean()
std_tg_w_married = married_female['twogirls'].std()

mean_ss_w_all = female['samesex'].mean()
std_ss_w_all = female['samesex'].std()
mean_ss_w_married = married_female['samesex'].mean()
std_ss_w_married = married_female['samesex'].std()

mean_twins_w_all = female['twins'].mean()
std_twins_w_all = female['twins'].std()
mean_twins_w_married = married_female['twins'].mean()
std_twins_w_married = married_female['twins'].std()

mean_age_w_all = female['age'].mean()
std_age_w_all = female['age'].std()
mean_age_w_married = married_female['age'].mean()
std_age_w_married = married_female['age'].std()
mean_age_m = married_male['age'].mean() 
std_age_m = married_male['age'].std()

mean_afb_w_all = female['agefirst'].mean()
std_afb_w_all = female['agefirst'].std()
mean_afb_w_married = married_female['agefirst'].mean()
std_afb_w_married = married_female['agefirst'].std()
mean_afb_m = married_male['agefirst'].mean()
std_afb_m = married_male['agefirst'].std()

mean_lf_w_all = female['labforce'].mean()
std_lf_w_all = female['labforce'].std()
mean_lf_w_married =  married_female['labforce'].mean()
std_lf_w_married =  married_female['labforce'].std()
mean_lf_m = married_male['labforce'].mean()
std_lf_m = married_male['labforce'].std()

mean_ww_w_all = female['wkswork2'].mean()
std_ww_w_all = female['wkswork2'].std()
mean_ww_w_married = married_female['wkswork2'].mean()
std_ww_w_married = married_female['wkswork2'].std()
mean_ww_m = married_male['wkswork2'].mean()
std_ww_m = married_male['wkswork2'].std()

mean_hw_w_all = female['hrswork2'].mean()
std_hw_w_all = female['hrswork2'].std()
mean_hw_w_married = married_female['hrswork2'].mean()
std_hw_w_married = married_female['hrswork2'].std()
mean_hw_m = married_male['hrswork2'].mean()
std_hw_m = married_male['hrswork2'].std()

mean_inc_w_all = female['inctot'].mean()
std_inc_w_all = female['inctot'].std()
mean_inc_w_married = married_female['inctot'].mean()
std_inc_w_married = married_female['inctot'].std()
mean_inc_m = married_male['inctot'].mean()
std_inc_m = married_male['inctot'].std()

mean_finc_w_all = female['ftotinc'].mean()
std_finc_w_all = female['ftotinc'].std()
mean_finc_married = married_female['ftotinc'].mean()
std_finc_w_married = married_female['ftotinc'].std()
mean_finc_m = married_male['ftotinc'].mean()
std_finc_ml = married_male['ftotinc'].std()

mean_nwinc = df['nonwifeinc'].mean()
std_nwinc = df['nonwifeinc'].std()

#print all means and stds
print(mean_nchild_w_all, std_nchild_w_all)
print(mean_nchild_w_married,  std_nchild_w_married)
print(mean_mt2_w_all, std_mt2_w_all)
print(mean_mt2_w_all, std_mt2_w_all)
print(mean_fbm_w_all, std_fbm_w_all)
print(mean_fbm_w_married, std_fbm_w_married)
print(mean_sbm_w_all, std_sbm_w_all)
print(mean_sbm_w_married, std_sbm_w_married)
print(mean_tb_w_all, std_tb_w_all)
print(mean_tb_w_married, std_tb_w_married)
print(mean_tg_w_all, std_tg_w_all)
print(mean_tg_w_married, std_tg_w_married)
print(mean_ss_w_all, std_ss_w_all)
print(mean_ss_w_married, std_ss_w_married)
print(mean_twins_w_all, std_twins_w_all)
print(mean_twins_w_married, std_twins_w_married)
print(mean_age_w_all, std_age_w_all)
print(mean_age_w_married, std_age_w_married)
print(mean_age_m, std_age_m)
print(mean_afb_w_all, std_afb_w_all)
print(mean_afb_w_married, std_afb_w_married)
print(mean_afb_m, std_afb_m)
print(mean_lf_w_all, std_lf_w_all)
print(mean_lf_w_married, std_lf_w_married)
print(mean_lf_m, std_lf_m)
print(mean_ww_w_all, std_ww_w_all)
print(mean_ww_w_married, std_ww_w_married)
print(mean_ww_m, std_ww_m)
print(mean_hw_w_all, std_hw_w_all)
print(mean_hw_w_married, std_hw_w_married)
print(mean_hw_m, std_hw_m)
print(mean_inc_w_all, std_inc_w_all)
print(mean_inc_w_married, std_inc_w_married)
print(mean_inc_m, std_inc_m)
print(mean_finc_w_all, std_finc_w_all)
print(mean_finc_married, std_finc_w_married)
print(mean_finc_m, std_finc_ml)
print(mean_nwinc, std_nwinc)
print(female_rows, married_female_rows, married_male_rows)

print(df['sex'].value_counts())