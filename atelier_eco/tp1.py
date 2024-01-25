import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv('atelier_eco/data/Ex_Travail1.csv', sep=',', header=0)

#store the columns of the df in a dictionnary as the keys and the datatype of the column as the values
col = data.columns
col_type = data.dtypes
col_dict = dict(
    zip(
        col,
        col_type,
        )
    )

#keep only records where age_12 is == "25 to 29 years", or == "45 to 49 years", or =="40 to 44 years", or == "50 to 54 years", or == "35 to 39 years", or == "30 to 34 years"
data_25_55 = data[
    (data['age_12'] == "25 to 29 years")
    | (data['age_12'] == "45 to 49 years")
    | (data['age_12'] == "40 to 44 years")
    | (data['age_12'] == "50 to 54 years")
    | (data['age_12'] == "35 to 39 years")
    | (data['age_12'] == "30 to 34 years")
    ]

#create a tenure_sqrd variable that represents tenure column squarred
data_25_55['tenure_sqrd'] = data_25_55['tenure']**2

#print data_25_55 with tenure and tenure_sqrd columns
print(data_25_55[['tenure', 'tenure_sqrd']])

#print all possible values for educ
dummy_var = data_25_55['educ'].unique()

def create_01_var_from(df, target_col, value, new_col):
    df[new_col] = np.where(
        df[target_col] == value, 1, 0
        )
    return df

data_w_dummy = create_01_var_from(
    data_25_55,
    'educ',
    "Baccalauréat",
    'bac'
    )
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "Diplôme ou certificat universitaire supérieur au baccalauréat",
    'more_than_bac'
    )
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "Études secondaires complétées",
    'secondaire'
)
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "Études postsecondaires partielles",
    'partial_post_secondaire'
)
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "Diplôme ou certificat d'études postsecondaires",
    'post_secondaire'
)
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "Études secondaires partielles",
    'no_secondaire'
)

#select only these columns: lwage, tenure, tenure_sqrd, bac, more_than_bac, secondaire, partial_post_secondaire, post_secondaire, no_secondaire
select_data = data_w_dummy[
    [
        'lwage',
        'tenure',
        'tenure_sqrd',
        'bac',
        'more_than_bac',
        'secondaire',
        'partial_post_secondaire',
        'post_secondaire',
        'no_secondaire'
        ]
    ]
select_data_gender = data_w_dummy[
    [
        'lwage',
        'tenure',
        'tenure_sqrd',
        'bac',
        'more_than_bac',
        'secondaire',
        'partial_post_secondaire',
        'post_secondaire',
        'no_secondaire',
        'femme'
        ]
    ]
#drop all rows with missing values
cleaned_data = select_data.dropna()
cleaned_data_gender = select_data_gender.dropna()
#print both number of rows in cleaned_data and cleaned_data_gender
print(cleaned_data.shape[0])
print(cleaned_data_gender.shape[0])

#number of records: 26334

#create a linear regression model that assesses the impact of tenure, tenure_sqrd, bac, more_than_bac, secondaire, partial_post_secondaire, post_secondaire, no_secondaire on lwage

model = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire", data=cleaned_data)
results = model.fit()
print(
    results.summary()
    )

#--------------------------------------------

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                  lwage   R-squared:                       0.197
# Model:                            OLS   Adj. R-squared:                  0.197
# Method:                 Least Squares   F-statistic:                     808.5
# Date:                Thu, 25 Jan 2024   Prob (F-statistic):               0.00
# Time:                        09:37:20   Log-Likelihood:                -12441.
# No. Observations:               26334   AIC:                         2.490e+04
# Df Residuals:                   26325   BIC:                         2.497e+04
# Df Model:                           8
# Covariance Type:            nonrobust
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# Intercept                   7.4513      0.027    275.971      0.000       7.398       7.504
# tenure                      0.0029      0.000     25.030      0.000       0.003       0.003
# tenure_sqrd             -5.635e-06   4.77e-07    -11.817      0.000   -6.57e-06    -4.7e-06
# bac                         0.4536      0.027     16.749      0.000       0.401       0.507
# more_than_bac               0.5982      0.028     21.639      0.000       0.544       0.652
# secondaire                  0.1443      0.027      5.279      0.000       0.091       0.198
# partial_post_secondaire     0.1772      0.029      6.063      0.000       0.120       0.234
# post_secondaire             0.2906      0.027     10.794      0.000       0.238       0.343
# no_secondaire               0.1006      0.030      3.407      0.001       0.043       0.158
# ==============================================================================
# Omnibus:                       70.638   Durbin-Watson:                   2.003
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):               91.341
# Skew:                           0.005   Prob(JB):                     1.46e-20
# Kurtosis:                       3.288   Cond. No.                     6.93e+05
# ==============================================================================


#--------------------------------------------

#reponse question 3 #1: le coef associe a bac est de 0.4536 et le coef de no_secondaire est de 0.1006. on peux donc observer que le fait davoir un bac versus avoir le plus petit niveau deducation possible (no_secondaire) augmente le log du salaire de 0.4536-0.1006 = 0.353

#redo the same regression with cleaned_data_gender but also adding the dummy variable femme
model2 = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire + femme", data=cleaned_data_gender)

results2 = model2.fit()
print(results2.summary())

#--------------------------------------------

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                  lwage   R-squared:                       0.230
# Model:                            OLS   Adj. R-squared:                  0.229
# Method:                 Least Squares   F-statistic:                     872.4
# Date:                Thu, 25 Jan 2024   Prob (F-statistic):               0.00
# Time:                        09:37:20   Log-Likelihood:                -11897.
# No. Observations:               26334   AIC:                         2.381e+04
# Df Residuals:                   26324   BIC:                         2.390e+04
# Df Model:                           9
# Covariance Type:            nonrobust
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# Intercept                   7.5017      0.026    283.172      0.000       7.450       7.554
# tenure                      0.0029      0.000     25.780      0.000       0.003       0.003
# tenure_sqrd             -5.616e-06   4.67e-07    -12.023      0.000   -6.53e-06    -4.7e-06
# bac                         0.4928      0.027     18.557      0.000       0.441       0.545
# more_than_bac               0.6330      0.027     23.361      0.000       0.580       0.686
# secondaire                  0.1560      0.027      5.827      0.000       0.104       0.208
# partial_post_secondaire     0.1956      0.029      6.834      0.000       0.140       0.252
# post_secondaire             0.3145      0.026     11.919      0.000       0.263       0.366
# no_secondaire               0.0986      0.029      3.410      0.001       0.042       0.155
# femme                      -0.1578      0.005    -33.333      0.000      -0.167      -0.149
# ==============================================================================
# Omnibus:                      134.232   Durbin-Watson:                   2.003
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              185.654
# Skew:                          -0.050   Prob(JB):                     4.85e-41
# Kurtosis:                       3.399   Cond. No.                     6.93e+05
# ==============================================================================


#--------------------------------------------
#reponse question 3 #2: le coef de femme est de  -0.1578. on peux donc observer que le fait detre une femme versus un homme diminue le log du salaire de 0.1578

#using cleaned_data_gender create a new variable, bac_homme which will be 0 if femme = 1 or bac == 0 and 1 otherwise
cleaned_data_gender['bac_homme'] = np.where((cleaned_data_gender["femme"] == 0) & (cleaned_data_gender["bac"] == 1), 1, 0)
cleaned_data_gender['bac_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["bac"] == 1), 1, 0)

model3 = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire + femme + bac_homme + bac_femme", data=cleaned_data_gender)
results3 = model3.fit()
print(results3.summary())

#--------------------------------------------

#                            OLS Regression Results
# ==============================================================================
# Dep. Variable:                  lwage   R-squared:                       0.233
# Model:                            OLS   Adj. R-squared:                  0.232
# Method:                 Least Squares   F-statistic:                     798.4
# Date:                Thu, 25 Jan 2024   Prob (F-statistic):               0.00
# Time:                        09:37:20   Log-Likelihood:                -11846.
# No. Observations:               26334   AIC:                         2.371e+04
# Df Residuals:                   26323   BIC:                         2.380e+04
# Df Model:                          10
# Covariance Type:            nonrobust
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# Intercept                   7.5116      0.026    283.892      0.000       7.460       7.563
# tenure                      0.0029      0.000     25.729      0.000       0.003       0.003
# tenure_sqrd             -5.599e-06   4.66e-07    -12.010      0.000   -6.51e-06   -4.69e-06
# bac                         0.3270      0.018     18.503      0.000       0.292       0.362
# more_than_bac               0.6391      0.027     23.623      0.000       0.586       0.692
# secondaire                  0.1580      0.027      5.914      0.000       0.106       0.210
# partial_post_secondaire     0.1988      0.029      6.958      0.000       0.143       0.255
# post_secondaire             0.3187      0.026     12.100      0.000       0.267       0.370
# no_secondaire               0.0983      0.029      3.404      0.001       0.042       0.155
# femme                      -0.1853      0.005    -33.974      0.000      -0.196      -0.175
# bac_homme                   0.1084      0.010     10.399      0.000       0.088       0.129
# bac_femme                   0.2185      0.010     21.128      0.000       0.198       0.239
# ==============================================================================
# Omnibus:                      137.879   Durbin-Watson:                   2.002
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              192.869
# Skew:                          -0.047   Prob(JB):                     1.32e-42
# Kurtosis:                       3.409   Cond. No.                     2.37e+18
# ==============================================================================
#--------------------------------------------

#reponse question 3 #3 et #4: le coef de bac_homme est 0.1084 et femme_bac est 0.2185. on peux donc observer que la dif entre bac_homme et bac_femme est de 0.2185-0.1084 = 0.1101. on peux donc observer que le fait detre une femme avec un bac versus un homme avec un bac augmente le log du salaire de 0.1101

# reponse question 3 #5: soit le  model2 (lwage = b0 + b1(tenure) + b2(tenure_sqrd) + ... + b9(femme)), si on derrive par wage on a Dlwage/DU = b1 + 2b2(tenure) -> CPO -> 0 = b1 + 2 (b2)(tenure) -> b1 = 2 (b2)(tenure) -> b1/(2 (b2)) = tenure
#donce tenure = 0.0029 / 2 (-5.616e-06) = -258.5