import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.sandbox.regression.gmm import IV2SLS

df = pd.read_stata('/Users/gabrielderome/Desktop/tp/econometrie/TP2/data_angrist_evans.dta')

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
print('\nTABLEAU2\n')
for x in target_cols:
    print('\n', x, ':')
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
    
target_list = ['morethantwo', 'nchild', 'labforce', 'wkswork2', 'hrswork2', 'inctot', 'ftotinc',]

print("\n TABLEAU5")
for x in target_list:
    print("\n", x)
    all_mean = female[x].mean()
    same_sex_mean = samesex_df[x].mean()
    dif = all_mean - same_sex_mean
    print(dif)
    
instrument1 = 'samesex'
instrument2 = ['twoboys', 'twogirls']

dependent_var = 'labforce'

regressed_var_list = ['wkswork2', 'hrswork2', 'inctot', 'ftotinc']
print("\nTABLEAU7 :\n")
print("\nOLS :\n")

#regress the variables in regressed_var_list on labforce using ols
ols_model = sm.OLS.from_formula("labforce ~ wkswork2 + hrswork2 + inctot + ftotinc", data=female)
#print the summary of the model
print(ols_model.fit().summary())

#regress using 2sls with samesex as instrument
print("\n2SLS with samesex as instrument :\n")
model1_2sls = IV2SLS(female[dependent_var], female[regressed_var_list], female[instrument1]).fit()
#print the summary of the model
print(model1_2sls.summary())

# regress using 2sls with twoboys and twogirls as instruments
print("\n2SLS with twoboys and twogirls as instruments :\n")
model2_2sls = IV2SLS(female[dependent_var], female[regressed_var_list], female[instrument2]).fit()
print(model2_2sls.summary())


#resultats:

# TABLEAU2


#  nchild :
# all : 2.5094147886902984 ( 0.8027259667221552 )
# married : 2.5094147886902984 ( 0.8027259667221552 )

#  morethantwo :
# all : 0.3684021758622751 ( 0.48237604529566835 )
# married : 0.3684021758622751 ( 0.48237604529566835 )

#  firstborn_male :
# all : 0.5179827 ( 0.4996815 )
# married : 0.5179827 ( 0.4996815 )

#  secondborn_male :
# all : 0.46091616 ( 0.49847507 )
# married : 0.46091616 ( 0.49847507 )

#  twoboys :
# all : 0.7387171976806742 ( 0.43933807654976775 )
# married : 0.7387171976806742 ( 0.43933807654976775 )

#  twogirls :
# all : 0.7088289796162353 ( 0.4543066913254173 )
# married : 0.7088289796162353 ( 0.4543066913254173 )

#  samesex :
# all : 0.9995417139896786 ( 0.02140292297372684 )
# married : 0.9995417139896786 ( 0.02140292297372684 )

#  twins :
# all : 0.017514495785761253 ( 0.1311795757821523 )
# married : 0.017514495785761253 ( 0.1311795757821523 )

#  age :
# all : 30.32542291828561 ( 3.53654876382893 )
# married : 30.32542291828561 ( 3.53654876382893 )

#  agefirst :
# all : 21.55030187100245 ( 3.882802077519895 )
# married : 21.55030187100245 ( 3.882802077519895 )

#  labforce :
# all : 0.3867933927112599 ( 0.4870205233564051 )
# married : 0.3867933927112599 ( 0.4870205233564051 )

#  wkswork2 :
# all : 26.341562556040408 ( 22.532976819062 )
# married : 26.341562556040408 ( 22.532976819062 )

#  hrswork2 :
# all : 19.05429692948373 ( 19.465516670137156 )
# married : 19.05429692948373 ( 19.465516670137156 )

#  inctot :
# all : 8693.974395759858 ( 10908.036367916084 )
# married : 8693.974395759858 ( 10908.036367916084 )

#  ftotinc :
# all : 33781.36435730368 ( 27603.34527853466 )
# married : 33781.36435730368 ( 27603.34527853466 )

#  nonwifeinc :
# all : 25087.389961543828 ( 25299.478219722903 )
# married : 25087.389961543828 ( 25299.478219722903 )

# sample size for all women : 50187
# sample size for married women : 50187

# TABLEAU3

# oneofboth ratio_all : 0.4985354773148425
# oneofboth ratio_married : 0.4985354773148425
# twoboys ratio_all : 0.7387171976806742
# twoboys ratio_married : 0.7387171976806742
# twogirls ratio_all : 0.7088289796162353
# twogirls ratio_married : 0.7088289796162353
# samesex ratio_all : 0.9995417139896786
# samesex ratio_married : 0.9995417139896786

#  TABLEAU4

#  age
# 0.0005285717422722769

#  agefirst
# -0.005953611016526139

#  black
# 0.0

#  white
# -3.0278275079287376e-05

#  other_race
# -2.9961304103889863e-06

#  hisp
# 0.0

#  TABLEAU5

#  morethantwo
# -0.00012904174397643242

#  nchild
# -0.00019369548161751737

#  labforce
# -7.767020238336197e-05

#  wkswork2
# 0.0057540080777265246

#  hrswork2
# 0.0031546760749101566

#  inctot
# 4.526604515142026

#  ftotinc
# 15.114935407502344

# TABLEAU7 :


# OLS :

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:               labforce   R-squared:                       0.660
# Model:                            OLS   Adj. R-squared:                  0.660
# Method:                 Least Squares   F-statistic:                 2.433e+04
# Date:                Fri, 14 Apr 2023   Prob (F-statistic):               0.00
# Time:                        01:38:54   Log-Likelihood:                -8050.0
# No. Observations:               50187   AIC:                         1.611e+04
# Df Residuals:                   50182   BIC:                         1.615e+04
# Df Model:                           4                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.8210      0.002    342.734      0.000       0.816       0.826
# wkswork2      -0.0075   8.54e-05    -87.642      0.000      -0.008      -0.007
# hrswork2      -0.0141   9.23e-05   -152.734      0.000      -0.014      -0.014
# inctot      2.023e-06    1.6e-07     12.667      0.000    1.71e-06    2.34e-06
# ftotinc     4.108e-07   5.04e-08      8.154      0.000    3.12e-07    5.09e-07
# ==============================================================================
# Omnibus:                     8362.265   Durbin-Watson:                   1.983
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):            13356.928
# Skew:                          -1.164   Prob(JB):                         0.00
# Kurtosis:                       3.984   Cond. No.                     8.44e+04
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 8.44e+04. This might indicate that there are
# strong multicollinearity or other numerical problems.

# 2SLS with samesex as instrument :

# /Users/gabrielderome/Library/Python/3.9/lib/python/site-packages/statsmodels/regression/linear_model.py:1854: RuntimeWarning: invalid value encountered in sqrt
#   return np.sqrt(np.diag(self.cov_params()))
#                           IV2SLS Regression Results                           
# ==============================================================================
# Dep. Variable:               labforce   R-squared:                     -88.734
# Model:                         IV2SLS   Adj. R-squared:                -88.742
# Method:                     Two Stage   F-statistic:                       nan
#                         Least Squares   Prob (F-statistic):                nan
# Date:                Fri, 14 Apr 2023                                         
# Time:                        01:38:54                                         
# No. Observations:               50187                                         
# Df Residuals:                   50183                                         
# Df Model:                           4                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# wkswork2      -0.1436        nan        nan        nan         nan         nan
# hrswork2       0.1238        nan        nan        nan         nan         nan
# inctot         0.0006        nan        nan        nan         nan         nan
# ftotinc    -9.722e-05        nan        nan        nan         nan         nan
# ==============================================================================
# Omnibus:                    27081.933   Durbin-Watson:                   1.944
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):           989395.024
# Skew:                          -1.972   Prob(JB):                         0.00
# Kurtosis:                      24.391   Cond. No.                     3.91e+03
# ==============================================================================

# 2SLS with twoboys and twogirls as instruments :

#                           IV2SLS Regression Results                           
# ==============================================================================
# Dep. Variable:               labforce   R-squared:                   -6197.519
# Model:                         IV2SLS   Adj. R-squared:              -6198.013
# Method:                     Two Stage   F-statistic:                       nan
#                         Least Squares   Prob (F-statistic):                nan
# Date:                Fri, 14 Apr 2023                                         
# Time:                        01:38:54                                         
# No. Observations:               50187                                         
# Df Residuals:                   50183                                         
# Df Model:                           4                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# wkswork2      -2.2815    1.3e+06  -1.76e-06      1.000   -2.54e+06    2.54e+06
# hrswork2       0.6786   2.89e+06   2.35e-07      1.000   -5.67e+06    5.67e+06
# inctot         0.0005   3358.331   1.49e-07      1.000   -6582.366    6582.367
# ftotinc        0.0012    177.284   7.03e-06      1.000    -347.478     347.481
# ==============================================================================
# Omnibus:                    15556.057   Durbin-Watson:                   1.811
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):           107472.714
# Skew:                          -1.315   Prob(JB):                         0.00
# Kurtosis:                       9.669   Cond. No.                     3.91e+03
# ==============================================================================