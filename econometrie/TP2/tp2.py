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

#create new column where ftotinc - inctot
df['nonwifeinc'] = df['ftotinc'] - df['inctot']

#create column oneofboth where true if firstborn_male != secondborn_male
df['oneofboth'] = df['firstborn_male'] != df['secondborn_male']
#convert oneofboth to int
df['oneofboth'] = df['oneofboth'].astype(int)

#create column for balck (1 where race == 'Black' else 0) and a column with white (1 where race == 'White' else 0)
df['black'] = df['race'] == 'Black'
df['white'] = df['race'] == 'White'
#convert black and white to int
df['black'] = df['black'].astype(int)
df['white'] = df['white'].astype(int)
#create column for hispanic where 1 if race == 'Hispanic' else 0
df['hisp'] = df['race'] == 'Hispanic'
df['other_race'] = df['race'] == 'Other race, nec'
#convert hisp and other_race to int
df['hisp'] = df['hisp'].astype(int)
df['other_race'] = df['other_race'].astype(int)


#create df where only sex == 'Female'
female = df.loc[df['sex'] == 'Female']
married_female = df.loc[df['married'] == 1]

#get the number of rows in each df
female_rows = female.shape[0]
married_female_rows = married_female.shape[0]

target_cols = ['nchild', 'morethantwo', 'firstborn_male', 'secondborn_male', 'twoboys', 'twogirls', 'samesex', 'twins',"age", 'agefirst', 'labforce', 'wkswork2', 'hrswork2', 'inctot', 'ftotinc', 'nonwifeinc']

for x in target_cols:
    print('\nTABLEAU2\n')
    mean_all_woman = female[x].mean()
    std_all_woman = female[x].std()
    mean_married_women = married_female[x].mean()
    std_married_women = married_female[x].std()
    print('all :', mean_all_woman, "(", std_all_woman, ")")
    print('married :', mean_married_women, "(", std_married_women, ")")
    
print("\nsample size for all women :", female.shape[0])
print("sample size for married women :", married_female.shape[0])
print('\nTABLEAU3\n')


target_cols = ['oneofboth', 'twoboys', 'twogirls', 'samesex']
for x in target_cols:
    print(x, 'ratio_all :', female[x].mean())
    print(x, 'ratio_married :', married_female[x].mean())

#compute the diference in mean for 'age', 'agefirst', 'black', 'white', 'Other_race', 'hisp'

target_list = ['age', 'agefirst', 'black', 'white', 'other_race', 'hisp']

samesex_df = df.loc[df['samesex'] == 1]
print("\n TABLEAU4")
for x in target_list:
    print("\n", x)
    all_mean = female[x].mean()
    same_sex_mean = samesex_df[x].mean()
    dif =  all_mean - same_sex_mean
    print(dif)
    