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

#add all unique values from prov in a list
prov_unique_pre = df['prov'].unique()

#change all the values in the column prov where 'Qu\x8fbec' to '2' and where 'Ontario' to '1'
df['prov'] = df['prov'].replace('Qu\x8fbec', '2')
df['prov'] = df['prov'].replace('Ontario', '1')

#add all unique values from prov in a list
prov_unique_post = df['prov'].unique()

#get the average of lnwage where recensement is 1986
lnwage_1986 = df[df['recensement'] == 1986]['lnwage'].mean()
#get the average of lnwage where recensement is 2006
lnwage_2006 = df[df['recensement'] == 2006]['lnwage'].mean()
#get the change in lnwage between 1986 and 2006 in %
change = (lnwage_2006 - lnwage_1986)/lnwage_1986 * 100
print("Numero 1-a):")
print('----------------------------------------------------------------')
#print both averages and the change
print("average lnwage in 1986: ", lnwage_1986)
print("average lnwage in 2006: ", lnwage_2006)
print("change in lnwage between 1986 and 2006: ", change, "%")
print('----------------------------------------------------------------')
print("\n\n")
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
ratio = bac/size[0] * 100
#print the size of the sample, the number of people with a bachelors  and the ratio of people with a bachelor degree
print("Numero 1-c):")
print("----------------------------------------------------------------")
print("size of the sample: ", size[0])
print("number of people with a bachelor degree: ", bac)
print("ratio of people with a bachelor degree: ", ratio, "%")
print("----------------------------------------------------------------")
print("\n\n")
#create binary variables for dgmfspnum, dgreepnum, recensement and prov and count the number of new columns
df = pd.get_dummies(df, columns=['dgmfspnum', 'dgreepnum', 'recensement', 'prov'])
print("Numero 1-d):")
print("----------------------------------------------------------------")
print("number of new columns: ", df.shape[1])
print("----------------------------------------------------------------")
print("\n\n")
print("Numero 2-a):")
print("----------------------------------------------------------------")
#compute linear regression of lnwage on bac where recensement is 2006
model1 = sm.OLS.from_formula("lnwage ~ bac + recensement_2006", data=df)
#display the model
print(model1.fit().summary())
#get the coefficient of bac and print it
print("coefficient of bac: ", model1.fit().params[1])
print("----------------------------------------------------------------")
print("\n\n")
print("Numero 2-b):")
print("----------------------------------------------------------------")
#compute the linear regression of lnwage on bac, agep, and agep**2 where recensement is 2006
model2 = sm.OLS.from_formula("lnwage ~ bac + agep + agep**2 + recensement_2006", data=df)
#display the model2
print(model2.fit().summary())
print("coefficient of bac: ", model2.fit().params[1])
#print the coeficient of age and age**2
print("coefficient of age: ", model2.fit().params[2])
print("coefficient of age**2: ", model2.fit().params[3])
print("----------------------------------------------------------------")
print("\n\n")
print("Numero 2-c):")
print("----------------------------------------------------------------")
#compute the linear regression of lnwage on bac, agep, and agep**2 and the binary variables for prov where recensement is 2006
model3 = sm.OLS.from_formula("lnwage ~ bac + agep + agep**2 + recensement_2006 + prov_1 + prov_2 + prov_3 + prov_4 + prov_5 + prov_6 + prov_7 + prov_8 + prov_9 + prov_10", data=df)
#display the model3
print(model3.fit().summary())
print("coefficient of bac: ", model3.fit().params[1])
#test wether lnwage and the binary variables for prov are jointly significant
test1 = model3.fit().f_test("prov_1 = prov_2 = prov_3 = prov_4 = prov_5 = prov_6 = prov_7 = prov_8 = prov_9 = prov_10 = 0")
print(test1)
#print the coefficient of bac
print("----------------------------------------------------------------")
print("\n\n")
print("Numero 2-d):")
print("----------------------------------------------------------------")
#create dummy variable for bac_1986 and bac_2006
df['bac_1986'] = np.where((df['bac'] == 1) & (df['recensement_1986'] == 1), 1, 0)
df['bac_2006'] = np.where((df['bac'] == 1) & (df['recensement_2006'] == 1), 1, 0)
df_w_bac = df
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

print("----------------------------------------------------------------")
print("Numero 2-e):")

#get the coeficient of every field of study (dgmfspnum) in 2006
for i in range(1, 11):  
    print("coefficient of dgmfspnum_", i, ": ", model3.fit().params[i+3])
print("----------------------------------------------------------------")


#RESULTS
# Numero 1-a):
# ----------------------------------------------------------------
# average lnwage in 1986:  6.397754
# average lnwage in 2006:  6.5708995
# change in lnwage between 1986 and 2006:  2.706344984471798 %
# ----------------------------------------------------------------



# Numero 1-c):
# ----------------------------------------------------------------
# size of the sample:  115910
# number of people with a bachelor degree:  42776
# ratio of people with a bachelor degree:  36.904494866706926 %
# ----------------------------------------------------------------



# Numero 1-d):
# ----------------------------------------------------------------
# number of new columns:  33
# ----------------------------------------------------------------



# Numero 2-a):
# ----------------------------------------------------------------
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                 lnwage   R-squared:                       0.149
# Model:                            OLS   Adj. R-squared:                  0.149
# Method:                 Least Squares   F-statistic:                 1.016e+04
# Date:                Thu, 02 Mar 2023   Prob (F-statistic):               0.00
# Time:                        13:27:48   Log-Likelihood:                -95576.
# No. Observations:              115910   AIC:                         1.912e+05
# Df Residuals:                  115907   BIC:                         1.912e+05
# Df Model:                           2                                         
# Covariance Type:            nonrobust                                         
# ====================================================================================
#                        coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------------
# Intercept            6.2676      0.003   2179.156      0.000       6.262       6.273
# bac                  0.4503      0.003    130.438      0.000       0.444       0.457
# recensement_2006     0.0912      0.004     25.929      0.000       0.084       0.098
# ==============================================================================
# Omnibus:                     3515.361   Durbin-Watson:                   1.988
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9338.995
# Skew:                          -0.054   Prob(JB):                         0.00
# Kurtosis:                       4.386   Cond. No.                         3.38
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# coefficient of bac:  0.45029403748533453
# ----------------------------------------------------------------



# Numero 2-b):
# ----------------------------------------------------------------
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                 lnwage   R-squared:                       0.161
# Model:                            OLS   Adj. R-squared:                  0.161
# Method:                 Least Squares   F-statistic:                     7409.
# Date:                Thu, 02 Mar 2023   Prob (F-statistic):               0.00
# Time:                        13:27:49   Log-Likelihood:                -94770.
# No. Observations:              115910   AIC:                         1.895e+05
# Df Residuals:                  115906   BIC:                         1.896e+05
# Df Model:                           3                                         
# Covariance Type:            nonrobust                                         
# ====================================================================================
#                        coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------------
# Intercept            6.0088      0.007    854.448      0.000       5.995       6.023
# bac                  0.4766      0.003    136.563      0.000       0.470       0.483
# agep                 0.0065      0.000     40.277      0.000       0.006       0.007
# recensement_2006     0.0745      0.004     21.180      0.000       0.068       0.081
# ==============================================================================
# Omnibus:                     3647.594   Durbin-Watson:                   1.987
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9842.099
# Skew:                          -0.063   Prob(JB):                         0.00
# Kurtosis:                       4.422   Cond. No.                         184.
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# coefficient of bac:  0.4765820213135093
# coefficient of age:  0.006458794692210077
# coefficient of age**2:  0.0744722189569672
# ----------------------------------------------------------------



# Numero 2-c):
# ----------------------------------------------------------------
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                 lnwage   R-squared:                       0.172
# Model:                            OLS   Adj. R-squared:                  0.172
# Method:                 Least Squares   F-statistic:                     1855.
# Date:                Thu, 02 Mar 2023   Prob (F-statistic):               0.00
# Time:                        13:27:49   Log-Likelihood:                -93980.
# No. Observations:              115910   AIC:                         1.880e+05
# Df Residuals:                  115896   BIC:                         1.881e+05
# Df Model:                          13                                         
# Covariance Type:            nonrobust                                         
# ====================================================================================
#                        coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------------
# Intercept            6.2803      0.033    192.621      0.000       6.216       6.344
# bac                  0.4755      0.003    137.065      0.000       0.469       0.482
# agep                 0.0065      0.000     40.882      0.000       0.006       0.007
# recensement_2006     0.0709      0.003     20.271      0.000       0.064       0.078
# prov_1              -0.2221      0.032     -6.944      0.000      -0.285      -0.159
# prov_2              -0.2218      0.032     -6.875      0.000      -0.285      -0.159
# prov_3              -0.2564      0.032     -7.957      0.000      -0.320      -0.193
# prov_4              -0.3175      0.033     -9.545      0.000      -0.383      -0.252
# prov_5              -0.4835      0.035    -14.013      0.000      -0.551      -0.416
# prov_6              -0.3249      0.032    -10.138      0.000      -0.388      -0.262
# prov_7              -0.3245      0.033     -9.847      0.000      -0.389      -0.260
# prov_8              -0.3975      0.034    -11.864      0.000      -0.463      -0.332
# prov_9              -0.4246      0.033    -12.744      0.000      -0.490      -0.359
# prov_10             -0.4182      0.041    -10.282      0.000      -0.498      -0.338
# ==============================================================================
# Omnibus:                     3896.748   Durbin-Watson:                   1.987
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):            10734.403
# Skew:                          -0.085   Prob(JB):                         0.00
# Kurtosis:                       4.481   Cond. No.                     2.76e+03
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 2.76e+03. This might indicate that there are
# strong multicollinearity or other numerical problems.
# coefficient of bac:  0.4754902028844744
# <F test: F=159.16031460352767, p=0.0, df_denom=1.16e+05, df_num=10>
# ----------------------------------------------------------------



# Numero 2-d):
# ----------------------------------------------------------------
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                 lnwage   R-squared:                       0.170
# Model:                            OLS   Adj. R-squared:                  0.170
# Method:                 Least Squares   F-statistic:                     1826.
# Date:                Thu, 02 Mar 2023   Prob (F-statistic):               0.00
# Time:                        13:27:49   Log-Likelihood:                -94137.
# No. Observations:              115910   AIC:                         1.883e+05
# Df Residuals:                  115896   BIC:                         1.884e+05
# Df Model:                          13                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      6.3276      0.033    194.354      0.000       6.264       6.391
# bac_1986       0.4406      0.006     69.826      0.000       0.428       0.453
# bac_2006       0.5055      0.004    140.226      0.000       0.498       0.513
# agep           0.0068      0.000     43.135      0.000       0.007       0.007
# prov_1        -0.2428      0.032     -7.585      0.000      -0.306      -0.180
# prov_2        -0.2390      0.032     -7.403      0.000      -0.302      -0.176
# prov_3        -0.2745      0.032     -8.512      0.000      -0.338      -0.211
# prov_4        -0.3372      0.033    -10.129      0.000      -0.402      -0.272
# prov_5        -0.5040      0.035    -14.594      0.000      -0.572      -0.436
# prov_6        -0.3463      0.032    -10.797      0.000      -0.409      -0.283
# prov_7        -0.3443      0.033    -10.439      0.000      -0.409      -0.280
# prov_8        -0.4160      0.034    -12.406      0.000      -0.482      -0.350
# prov_9        -0.4440      0.033    -13.318      0.000      -0.509      -0.379
# prov_10       -0.4380      0.041    -10.759      0.000      -0.518      -0.358
# ==============================================================================
# Omnibus:                     3857.778   Durbin-Watson:                   1.983
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):            10639.709
# Skew:                          -0.078   Prob(JB):                         0.00
# Kurtosis:                       4.476   Cond. No.                     2.76e+03
# ==============================================================================

# Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 2.76e+03. This might indicate that there are
# strong multicollinearity or other numerical problems.
# coefficient of bac_1986:  6.327646124076698
# coefficient of bac_2006:  0.44059093011588674
# <F test: F=161.1078333837945, p=0.0, df_denom=1.16e+05, df_num=10>
# ----------------------------------------------------------------
# Numero 2-e):
# coefficient of dgmfspnum_ 1 :  -0.22209583973107208
# coefficient of dgmfspnum_ 2 :  -0.22176623044161892
# coefficient of dgmfspnum_ 3 :  -0.25641217772476127
# coefficient of dgmfspnum_ 4 :  -0.31746719704410187
# coefficient of dgmfspnum_ 5 :  -0.48352623813026513
# coefficient of dgmfspnum_ 6 :  -0.3249495858899716
# coefficient of dgmfspnum_ 7 :  -0.3245346109728783
# coefficient of dgmfspnum_ 8 :  -0.3974696478802598
# coefficient of dgmfspnum_ 9 :  -0.4245657654689932
# coefficient of dgmfspnum_ 10 :  -0.4181592369622698
# ----------------------------------------------------------------