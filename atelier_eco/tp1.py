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

#create a linear regression model that assesses the impact of tenure, tenure_sqrd, bac, more_than_bac, secondaire, partial_post_secondaire, post_secondaire, no_secondaire on lwage
model = sm.OLS(
    cleaned_data['lwage'],
    cleaned_data[
        [
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
    )
results = model.fit()
print(
    results.summary()
    )

#--------------------------------------------

#                                  OLS Regression Results                                
# =======================================================================================
# Dep. Variable:                  lwage   R-squared (uncentered):                   0.991
# Model:                            OLS   Adj. R-squared (uncentered):              0.991
# Method:                 Least Squares   F-statistic:                          3.534e+05
# Date:                Mon, 22 Jan 2024   Prob (F-statistic):                        0.00
# Time:                        13:54:14   Log-Likelihood:                         -30338.
# No. Observations:               26334   AIC:                                  6.069e+04
# Df Residuals:                   26326   BIC:                                  6.076e+04
# Df Model:                           8                                                  
# Covariance Type:            nonrobust                                                  
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# tenure                      0.0075      0.000     33.276      0.000       0.007       0.008
# tenure_sqrd              -2.17e-05   9.34e-07    -23.235      0.000   -2.35e-05   -1.99e-05
# bac                         7.7102      0.013    602.763      0.000       7.685       7.735
# more_than_bac               7.8624      0.017    471.949      0.000       7.830       7.895
# secondaire                  7.4093      0.014    511.906      0.000       7.381       7.438
# partial_post_secondaire     7.4467      0.025    298.313      0.000       7.398       7.496
# post_secondaire             7.5496      0.011    664.105      0.000       7.527       7.572
# no_secondaire               7.3711      0.026    280.017      0.000       7.319       7.423
# ==============================================================================
# Omnibus:                    32396.451   Durbin-Watson:                   1.985
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):          4451036.048
# Skew:                           6.769   Prob(JB):                         0.00
# Kurtosis:                      65.235   Cond. No.                     1.42e+05
# ==============================================================================

#--------------------------------------------

#reponse question 3 #1: le coef associe a bac est de 7.7102 et le coef de no_secondaire est de 7.3711. on peux donc observer que le fait davoir un bac versus avoir le plus petit niveau deducation possible (no_secondaire) augmente le salaire de 7.7102-7.3711 = 0.3391

#redo the same regression with cleaned_data_gender but also adding the dummy variable femme
model2 = sm.OLS(
    cleaned_data_gender['lwage'],
    cleaned_data_gender[
        [
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
    )
results2 = model2.fit()
print(results2.summary())

#--------------------------------------------

#                                 OLS Regression Results                                
# =======================================================================================
# Dep. Variable:                  lwage   R-squared (uncentered):                   0.991
# Model:                            OLS   Adj. R-squared (uncentered):              0.991
# Method:                 Least Squares   F-statistic:                          3.150e+05
# Date:                Mon, 22 Jan 2024   Prob (F-statistic):                        0.00
# Time:                        14:10:31   Log-Likelihood:                         -30301.
# No. Observations:               26334   AIC:                                  6.062e+04
# Df Residuals:                   26325   BIC:                                  6.069e+04
# Df Model:                           9                                                  
# Covariance Type:            nonrobust                                                  
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# tenure                      0.0076      0.000     33.449      0.000       0.007       0.008
# tenure_sqrd             -2.174e-05   9.33e-07    -23.317      0.000   -2.36e-05   -1.99e-05
# bac                         7.7557      0.014    560.590      0.000       7.729       7.783
# more_than_bac               7.9057      0.017    454.656      0.000       7.872       7.940
# secondaire                  7.4407      0.015    499.009      0.000       7.411       7.470
# partial_post_secondaire     7.4816      0.025    296.198      0.000       7.432       7.531
# post_secondaire             7.5872      0.012    623.313      0.000       7.563       7.611
# no_secondaire               7.3954      0.026    279.699      0.000       7.344       7.447
# femme                      -0.0814      0.010     -8.562      0.000      -0.100      -0.063
# ==============================================================================
# Omnibus:                    32672.154   Durbin-Watson:                   1.985
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):          4625601.888
# Skew:                           6.865   Prob(JB):                         0.00
# Kurtosis:                      66.459   Cond. No.                     1.49e+05
# ==============================================================================

#--------------------------------------------
#reponse question 3 #2: le coef de femme est de -0.0814. on peux donc observer que le fait detre une femme versus un homme diminue le salaire de 0.0814

#using cleaned_data_gender create a new variable, bac_homme which will be 0 if femme = 1 or bac == 0 and 1 otherwise
cleaned_data_gender['bac_homme'] = np.where((cleaned_data_gender["femme"] == 0) & (cleaned_data_gender["bac"] == 1), 1, 0)
cleaned_data_gender['bac_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["bac"] == 1), 1, 0)

#redo the regression with bac_homme and bac_femme instead of bac.
model3 = sm.OLS(
    cleaned_data_gender['lwage'],
    cleaned_data_gender[
        [
            'tenure',
            'tenure_sqrd',
            'more_than_bac',
            'secondaire',
            'partial_post_secondaire',
            'post_secondaire',
            'no_secondaire',
            'femme',
            'bac_homme',
            'bac_femme'
         ]
        ]
    )
results3 = model3.fit()
print(results3.summary())

#--------------------------------------------

#                                  OLS Regression Results                                
# =======================================================================================
# Dep. Variable:                  lwage   R-squared (uncentered):                   0.991
# Model:                            OLS   Adj. R-squared (uncentered):              0.991
# Method:                 Least Squares   F-statistic:                          2.835e+05
# Date:                Mon, 22 Jan 2024   Prob (F-statistic):                        0.00
# Time:                        14:48:20   Log-Likelihood:                         -30301.
# No. Observations:               26334   AIC:                                  6.062e+04
# Df Residuals:                   26324   BIC:                                  6.070e+04
# Df Model:                          10                                                  
# Covariance Type:            nonrobust                                                  
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# tenure                      0.0076      0.000     33.449      0.000       0.007       0.008
# tenure_sqrd             -2.174e-05   9.33e-07    -23.316      0.000   -2.36e-05   -1.99e-05
# more_than_bac               7.9049      0.018    447.409      0.000       7.870       7.940
# secondaire                  7.4401      0.015    492.944      0.000       7.411       7.470
# partial_post_secondaire     7.4809      0.025    294.652      0.000       7.431       7.531
# post_secondaire             7.5866      0.012    607.763      0.000       7.562       7.611
# no_secondaire               7.3949      0.027    278.988      0.000       7.343       7.447
# femme                      -0.0801      0.011     -7.301      0.000      -0.102      -0.059
# bac_homme                   7.7580      0.017    461.690      0.000       7.725       7.791
# bac_femme                   7.7527      0.019    416.634      0.000       7.716       7.789
# ==============================================================================
# Omnibus:                    32668.396   Durbin-Watson:                   1.985
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):          4623293.729
# Skew:                           6.864   Prob(JB):                         0.00
# Kurtosis:                      66.443   Cond. No.                     1.59e+05
# ==============================================================================

#--------------------------------------------

#reponse question 3 #3: le coef de bac_homme est 7.7580 et femme_bac est 7.7527. on peux donc observer le fait que la diference entre une homme avec un bac versus une femme avec un bac n'est pas si grande, cela peut indiquer que le fait detre une femme ne fait pas necessairement descendre le salaire espere une fois que le bac est obtenu. dans les deux cas si on compare a no_secondaire (le plus petit niveau d'eductaion disponible dont le coef est de 7.3949) on vois une diference de 7.7580 - 7.3949 = 0.3631 pour les hommes et 7.7527 - 7.3949 = 0.3578 pour les femmes. L'impacte davoir un bac est donc plus important que celui detre un homme ou une femme.