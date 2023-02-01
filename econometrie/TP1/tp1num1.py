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

#count all the rows
sample_size = df.shape[0]
print('Question 1 C): The sample size is now ' + str(sample_size))


#create new column '1996' that is 1 if recensement == 1996 and 0 otherwise
df['1986'] = df['recensement'].apply(lambda x: 1 if x == 1986 else 0)
#create new column '2006' that is 1 if recensement == 2006 and 0 otherwise
df['2006'] = df['recensement'].apply(lambda x: 1 if x == 2006 else 0)


dummy_count = 7

#create a new column for each values in prov and set it to 1 if prov == value and 0 otherwise
for value in df['prov'].unique():
    df[value] = df['prov'].apply(lambda x: 1 if x == value else 0)
    dummy_count += 1

#create a new column for each values in dgmfspnum and set it to 1 if dgmfspnum == value and 0 otherwise
for value in df['dgmfspnum'].unique():
    df[value] = df['dgmfspnum'].apply(lambda x: 1 if x == value else 0)
    dummy_count += 1

print('Question 1 D): The number of dummy variables is ' + str(dummy_count))
print(df.head())



# Question 1 a): The growth of lnwage between 1996 and 2006 is 1%
# Question 1 C): The sample size is now 173148
# Question 1 D): The number of dummy variables is 29
#      lnwage  recensement   id     prov  dgreepnum  dgmfspnum  agep  minid  bac  metier  college  ...  6  8  3  10  9  4  5  NaN  11  1  2
# 0  6.508437         1986  1.0  Ontario          1         11    43    1.0    0       0        0  ...  0  0  0   0  0  0  0  0.0   1  0  0
# 1  6.961799         1986  2.0  Ontario          3          5    57    1.0    0       0        1  ...  0  0  0   0  0  0  1  0.0   0  0  0
# 2  6.508389         1986  3.0        7          2         11    27    1.0    0       0        0  ...  0  0  0   0  0  0  0  0.0   1  0  0
# 3  6.258992         1986  4.0   Qubec          2         11    57    1.0    0       0        0  ...  0  0  0   0  0  0  0  0.0   1  0  0
# 5  6.797405         1986  6.0  Ontario          1         11    44    1.0    0       0        0  ...  0  0  0   0  0  0  0  0.0   1  0  0