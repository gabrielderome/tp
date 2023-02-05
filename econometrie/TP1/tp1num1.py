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
model1 = sm.OLS.from_formula("lnwage ~ bac + recensement_2006", data=df)
#display the model
print(model1.fit().summary())
#get the coefficient of bac and print it
print("coefficient of bac: ", model1.fit().params[1])
#compute the linear regression of lnwage on bac, agep, and agep**2 where recensement is 2006
model2 = sm.OLS.from_formula("lnwage ~ bac + agep + agep**2 + recensement_2006", data=df)
#display the model2
print(model2.fit().summary())
print("coefficient of bac: ", model2.fit().params[1])
#print the coeficient of age and age**2
print("coefficient of age: ", model2.fit().params[2])
print("coefficient of age**2: ", model2.fit().params[3])
#compute the linear regression of lnwage on bac, agep, and agep**2 and the binary variables for prov where recensement is 2006
model3 = sm.OLS.from_formula("lnwage ~ bac + agep + agep**2 + recensement_2006 + prov_1 + prov_2 + prov_3 + prov_4 + prov_5 + prov_6 + prov_7 + prov_8 + prov_9 + prov_10", data=df)
#display the model3
print(model3.fit().summary())
print("coefficient of bac: ", model3.fit().params[1])
#test wether lnwage and the binary variables for prov are jointly significant
test1 = model3.fit().f_test("prov_1 = prov_2 = prov_3 = prov_4 = prov_5 = prov_6 = prov_7 = prov_8 = prov_9 = prov_10 = 0")
print(test1)
#print the coefficient of bac
print("coefficient of bac: ", model3.fit().params[1])
#create dummy variable for bac_1986 and bac_2006
df['bac_1986'] = np.where((df['bac'] == 1) & (df['recensement_1986'] == 1), 1, 0)
df['bac_2006'] = np.where((df['bac'] == 1) & (df['recensement_2006'] == 1), 1, 0)
#drop the column bac
df = df.drop(columns=['bac'])
#compute the linear regression of lnwage on bac_1986, bac_2006, agep, and agep**2 and the binary variables for prov
model4 = sm.OLS.from_formula("lnwage ~ bac_1986 + bac_2006 + agep + agep**2 + prov_1 + prov_2 + prov_3 + prov_4 + prov_5 + prov_6 + prov_7 + prov_8 + prov_9 + prov_10", data=df)
#display the model4
print(model4.fit().summary())
#print the coeficient of bac_1986
print("coefficient of bac_1986: ", model4.fit().params[0])
#print the coeficient of bac_2006
print("coefficient of bac_2006: ", model4.fit().params[1])
#test wether lnwage and the binary variables for prov are jointly significant
test2 = model4.fit().f_test("prov_1 = prov_2 = prov_3 = prov_4 = prov_5 = prov_6 = prov_7 = prov_8 = prov_9 = prov_10 = 0")
print(test2)

df2 = pd.DataFrame({'question': ['bac', 'bac_1986', 'bac_2006', 'agep', 'agep**2', 'provinces'], '(2.a)': [model1.fit().params[1], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'], '(2.b)': [model2.fit().params[1], 'N/A', 'N/A', model2.fit().params[2], model2.fit().params[3], 'N/A'], '(2.c)': [model3.fit().params[1], 'N/A', 'N/A', model3.fit().params[2], model3.fit().params[3], test1], '(2.d)': ['N/A', model4.fit().params[0], model4.fit().params[1], model4.fit().params[2], model4.fit().params[3], test2]})

df2.to_csv(r'/Users/gabrielderome/Downloads/table.csv', index=False)