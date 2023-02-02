#get the data from "/Users/gabrielderome/Downloads/lnw_1986_2006.dta", "/Users/gabrielderome/Downloads/rec1986_96.dta" and "/Users/gabrielderome/Downloads/rec2001_2006.dta"
#using pandas read the 3 files as df
#concatenate the 3 files into one dataframe
import pandas as pd

#read data
df1 = pd.read_stata("/Users/gabrielderome/Downloads/lnw_1986_2006.dta")
df2 = pd.read_stata("/Users/gabrielderome/Downloads/rec1986_96.dta")
df3 = pd.read_stata("/Users/gabrielderome/Downloads/rec2001_2006.dta")

#concatonate df2 and df3 into df_other_variables
df_other_variables = pd.concat([df2, df3], axis=0)

#join df1 and df_other_variables into df on id and recensement
df = pd.merge(df1, df_other_variables, on=['id', 'recensement'])

#get mean lnwage in 1996
mean_ln_wage_1996 = df.loc[df['recensement'] == 1996, 'lnwage'].mean()

#get mean lnwage in 2006
mean_ln_wage_2006 = df.loc[df['recensement'] == 2006, 'lnwage'].mean()

#get the growth of lnwage between 1996 and 2006 in %
growth_ln_wage = (mean_ln_wage_2006 - mean_ln_wage_1996) / mean_ln_wage_1996 * 100

#round growth_ln_wage to the closest integer
growth_ln_wage = round(growth_ln_wage)

print("Question 1 a): The growth of lnwage between 1996 and 2006 is " + str(growth_ln_wage) + "%")

#drop all the rows that are not in the year 1986 or 2006 and where dgreepnum <= 7
df = df.loc[(df['recensement'] == 1986) | (df['recensement'] == 2006)]
df = df.loc[df['dgreepnum'] <= 7]

#create new column 'bac' that is 1 if dgreepnum >= 5 and 0 otherwise
df['bac'] = df['dgreepnum'].apply(lambda x: 1 if x >= 5 else 0)
#create new column 'metier' that is 1 if dgreepnum == 4 and 0 otherwise
df['metier'] = df['dgreepnum'].apply(lambda x: 1 if x == 4 else 0)
#create new column 'college' that is 1 if dgreepnum == 3 and 0 otherwise
df['college'] = df['dgreepnum'].apply(lambda x: 1 if x == 3 else 0)
#create new column 'highschool' that is 1 if dgreepnum == 2 and 0 otherwise
df['highschool'] = df['dgreepnum'].apply(lambda x: 1 if x == 2 else 0)
#create new column 'primary' that is 1 if dgreepnum == 1 and 0 otherwise
df['primary'] = df['dgreepnum'].apply(lambda x: 1 if x == 1 else 0)
#create new column prov1 that is 1 if prov == 'Ontario' and 0 otherwise
df['prov1'] = df['prov'].apply(lambda x: 1 if x == 'Ontario' else 0)
#create new column prov2 that is 1 if prov == 'Qubec' and 0 otherwise
df['prov2'] = df['prov'].apply(lambda x: 1 if x == 'Qubec' else 0)
#create new column prov3 that is 1 if prov == 3 and 0 otherwise
df['prov3'] = df['prov'].apply(lambda x: 1 if x == 3 else 0)
#create new column prov4 that is 1 if prov == 4 and 0 otherwise
df['prov4'] = df['prov'].apply(lambda x: 1 if x == 4 else 0)
#create new column prov5 that is 1 if prov == 5 and 0 otherwise
df['prov5'] = df['prov'].apply(lambda x: 1 if x == 5 else 0)
#create new column prov6 that is 1 if prov == 6 and 0 otherwise
df['prov6'] = df['prov'].apply(lambda x: 1 if x == 6 else 0)
#create new column prov7 that is 1 if prov == 7 and 0 otherwise
df['prov7'] = df['prov'].apply(lambda x: 1 if x == 7 else 0)
#create new column prov8 that is 1 if prov == 8 and 0 otherwise
df['prov8'] = df['prov'].apply(lambda x: 1 if x == 8 else 0)
#create new column prov9 that is 1 if prov == 9 and 0 otherwise
df['prov9'] = df['prov'].apply(lambda x: 1 if x == 9 else 0)
#create new column prov10 that is 1 if prov == 10 and 0 otherwise
df['prov10'] = df['prov'].apply(lambda x: 1 if x == 10 else 0)

#count all the rows
sample_size = df.shape[0]
print('Question 1 C): The sample size is now ' + str(sample_size))


#create new column '1996' that is 1 if recensement == 1996 and 0 otherwise
df['1986'] = df['recensement'].apply(lambda x: 1 if x == 1986 else 0)
#create new column '2006' that is 1 if recensement == 2006 and 0 otherwise
df['2006'] = df['recensement'].apply(lambda x: 1 if x == 2006 else 0)

dummy_count = 17

#create a new column for each values in dgmfspnum and set it to 1 if dgmfspnum == value and 0 otherwise
for value in df['dgmfspnum'].unique():
    df["dgmfspnum"+ str(value)] = df['dgmfspnum'].apply(lambda x: 1 if x == value else 0)
    dummy_count += 1

print('Question 1 D): The number of dummy variables is ' + str(dummy_count))
print(df.head())

#import LSE regression from statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

#regress lnwage on bac where recensement == 2006
model_2006_1 = ols(formula="lnwage ~ bac", data=df.loc[df['2006'] == 1]).fit()

#get the coefficient of bac in model_2006
coefficient_bac_2006_1 = model_2006_1.params['bac']

#print the coefficient of bac in model_2006_1
print("question 2 a) The coefficient of bac in model_2006 is " + str(coefficient_bac_2006_1))


#regress lnwage on bac, agep and agep**2 where recensement == 2006
model_2006_2 = ols(formula="lnwage ~ bac + agep + agep**2", data=df.loc[df['2006'] == 1]).fit()

#get the coefficient of bac in model_2006_2
coefficient_bac_2006_2 = model_2006_2.params['bac']

#show the coefficient of bac in model_2006_2
print("question 2 b) The coefficient of bac in model_2006_2 is " + str(coefficient_bac_2006_2))

#regress lnwage on bac, agep, agep**2, provOntario, provQubec, prov3, prov4, prov5, prov6, prov7 prov8, prov9, prov10 where recensement == 2006
model_2006_3 = ols(formula="lnwage ~ bac + agep + agep**2 + prov3 + prov4 + prov5 + prov6 + prov7 + prov8 + prov9 + prov10 + prov2 + prov1", data=df.loc[df['2006'] == 1]).fit()

#get the coefficient of bac in model_2006_3
coefficient_bac_2006_3 = model_2006_3.params['bac']

#print the coefficient of bac in model_2006_3
print("question 2 c) The coefficient of bac in model_2006_3 is " + str(coefficient_bac_2006_3))