import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# load data from paths
df1 = pd.read_stata("/Users/gabrielderome/Downloads/lnw_1986_2006.dta")
df2 = pd.read_stata("/Users/gabrielderome/Downloads/rec1986_96.dta")
df3 = pd.read_stata("/Users/gabrielderome/Downloads/rec2001_2006.dta")

#merge dataframe
df_other_variables = pd.concat([df2, df3], axis=0)
df = pd.merge(df1, df_other_variables, on=['id', 'recensement'])

#change all the values in the column prov where 'Qu\x8fbec' to '2' and where 'Ontario' to '1'
df['prov'] = df['prov'].replace('Qu\x8fbec', '2')
df['prov'] = df['prov'].replace('Ontario', '1')

#filter df to get only the fields where recensement is 1986 or 2006 and where dgreepnum is either '7' '6' '5' '2' '1'
df = df[(df['recensement'] == 1986) | (df['recensement'] == 2006)]
df = df[(df['dgreepnum'] == 7) | (df['dgreepnum'] == 6) | (df['dgreepnum'] == 5) | (df['dgreepnum'] == 2) | (df['dgreepnum'] == 1)]

#create new column 'bac' where the values are 1 if dgreepnum is '7' or '6' or '5' and 0 otherwise
df['bac'] = np.where((df['dgreepnum'] == 7) | (df['dgreepnum'] == 6) | (df['dgreepnum'] == 5), 1, 0)
#count the size of the sample
size = df.shape
#count the number of people with a bachelor degree
bac = df['bac'].sum()
#compute the ratio of people with a bachelor degree
ratio = bac/size[0]
#print the size of the sample, the number of people with a bachelors  and the ratio of people with a bachelor degree
print("size of the sample: ", size[0])
print("number of people with a bachelor degree: ", bac)
print("ratio of people with a bachelor degree: ", ratio)

#create binary variables for dgmfspnum, dgreepnum, recensement and prov and count the number of new columns
df = pd.get_dummies(df, columns=['dgmfspnum', 'dgreepnum', 'recensement', 'prov'])
print("number of new columns: ", df.shape[1])

#compute linear regression of lnwage on bac where recensement is 2006
model = sm.OLS.from_formula("lnwage ~ bac + recensement_2006", data=df)
#get the coefficient of bac and print it
result = model.fit()
print("coefficient of bac: ", result.params[1])
