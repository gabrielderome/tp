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

