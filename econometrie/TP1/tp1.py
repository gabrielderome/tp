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

#print df
print(df.head())

#drop all the rows that dgreepnum > 7
df = df.loc[df['dgreepnum'] <= 7]

#create new column 'bac' that is 1 if dgreepnum >= 5 and 0 otherwise
df['bac'] = df['dgreepnum'].apply(lambda x: 1 if x >= 5 else 0)


#print df
print(df.head())

#create new column '1996' that is 1 if recensement == 1996 and 0 otherwise
df['1986'] = df['recensement'].apply(lambda x: 1 if x == 1986 else 0)
#create new column '2006' that is 1 if recensement == 2006 and 0 otherwise
df['2006'] = df['recensement'].apply(lambda x: 1 if x == 2006 else 0)

#get unique values of prov
prov = df['prov'].unique()
print(prov)

#if prov == 'Ontario' change for 1 and if prov == 'Quebec' change for 2
df['prov'] = df['prov'].apply(lambda x: 1 if x == 'Ontario' else 2)

#print df
print(df.head())
