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
print(dummy_var)

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
data_w_dummy = create_01_var_from(
    data_w_dummy,
    'educ',
    "0 à 8 années",
    'none',
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
        'no_secondaire',
        'none'
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
        'none',
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

model = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire + none", data=cleaned_data)
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
# Date:                Fri, 26 Jan 2024   Prob (F-statistic):               0.00
# Time:                        00:47:26   Log-Likelihood:                -12441.
# No. Observations:               26334   AIC:                         2.490e+04
# Df Residuals:                   26325   BIC:                         2.497e+04
# Df Model:                           8
# Covariance Type:            nonrobust
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# Intercept                   6.7405      0.006   1194.044      0.000       6.729       6.752
# tenure                      0.0029      0.000     25.030      0.000       0.003       0.003
# tenure_sqrd             -5.635e-06   4.77e-07    -11.817      0.000   -6.57e-06    -4.7e-06
# bac                         1.1645      0.006    195.799      0.000       1.153       1.176
# more_than_bac               1.3090      0.008    171.567      0.000       1.294       1.324
# secondaire                  0.8551      0.007    127.193      0.000       0.842       0.868
# partial_post_secondaire     0.8880      0.011     79.293      0.000       0.866       0.910
# post_secondaire             1.0015      0.005    185.896      0.000       0.991       1.012
# no_secondaire               0.8115      0.012     68.831      0.000       0.788       0.835
# none                        0.7109      0.023     30.279      0.000       0.665       0.757
# ==============================================================================
# Omnibus:                       70.638   Durbin-Watson:                   2.003
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):               91.341
# Skew:                           0.005   Prob(JB):                     1.46e-20
# Kurtosis:                       3.288   Cond. No.                     9.65e+17
# ==============================================================================


#--------------------------------------------

#reponse question 3 #1: le coef associe a bac est de 1.1645 et le coef de none est de 0.7109. on peux donc observer que le fait davoir un bac versus avoir le plus petit niveau deducation possible (none) augmente le log du salaire de 1.1645-0.7109 = 0.4536, donc en % on a une augmentation de 45.36% du salaire.

#redo the same regression with cleaned_data_gender but also adding the dummy variable femme
model2 = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire + none + femme", data=cleaned_data_gender)

results2 = model2.fit()
print(results2.summary())

#--------------------------------------------

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                  lwage   R-squared:                       0.230
# Model:                            OLS   Adj. R-squared:                  0.229
# Method:                 Least Squares   F-statistic:                     872.4
# Date:                Fri, 26 Jan 2024   Prob (F-statistic):               0.00
# Time:                        00:47:26   Log-Likelihood:                -11897.
# No. Observations:               26334   AIC:                         2.381e+04
# Df Residuals:                   26324   BIC:                         2.390e+04
# Df Model:                           9
# Covariance Type:            nonrobust
# ===========================================================================================
#                               coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------
# Intercept                   6.8003      0.006   1169.743      0.000       6.789       6.812
# tenure                      0.0029      0.000     25.780      0.000       0.003       0.003
# tenure_sqrd             -5.616e-06   4.67e-07    -12.023      0.000   -6.53e-06    -4.7e-06
# bac                         1.1942      0.006    202.627      0.000       1.183       1.206
# more_than_bac               1.3344      0.008    177.625      0.000       1.320       1.349
# secondaire                  0.8574      0.007    130.181      0.000       0.844       0.870
# partial_post_secondaire     0.8970      0.011     81.742      0.000       0.876       0.919
# post_secondaire             1.0159      0.005    191.861      0.000       1.006       1.026
# no_secondaire               0.8000      0.012     69.246      0.000       0.777       0.823
# none                        0.7014      0.023     30.497      0.000       0.656       0.746
# femme                      -0.1578      0.005    -33.333      0.000      -0.167      -0.149
# ==============================================================================
# Omnibus:                      134.232   Durbin-Watson:                   2.003
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              185.654
# Skew:                          -0.050   Prob(JB):                     4.85e-41
# Kurtosis:                       3.399   Cond. No.                     9.63e+17
# ==============================================================================


#--------------------------------------------
#reponse question 3 #2: le coef de femme est de  -0.1578. on peux donc observer que le fait detre une femme versus un homme diminue en pourcentage du salaire de 15.78%

#using cleaned_data_gender create a new variable, bac_homme which will be 0 if femme = 1 or bac == 0 and 1 otherwise
cleaned_data_gender['bac_femme'] = np.where((cleaned_data_gender["femme"] == 0) & (cleaned_data_gender["bac"] == 1), 1, 0)
cleaned_data_gender['more_than_bac_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["more_than_bac"] == 1), 1, 0)
cleaned_data_gender['secondaire_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["secondaire"] == 1), 1, 0)
cleaned_data_gender['partial_post_secondaire_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["partial_post_secondaire"] == 1), 1, 0)
cleaned_data_gender['post_secondaire_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["post_secondaire"] == 1), 1, 0)
cleaned_data_gender['no_secondaire_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["no_secondaire"] == 1), 1, 0)
cleaned_data_gender['none_femme'] = np.where((cleaned_data_gender["femme"] == 1) & (cleaned_data_gender["none"] == 1), 1, 0)

model3 = sm.OLS.from_formula("lwage ~ tenure + tenure_sqrd + bac + more_than_bac + secondaire + partial_post_secondaire + post_secondaire + no_secondaire + none + femme + bac_femme + more_than_bac_femme + secondaire_femme + partial_post_secondaire_femme + post_secondaire_femme + no_secondaire_femme + none_femme", data=cleaned_data_gender)
results3 = model3.fit()
print(results3.summary())

#--------------------------------------------

#                             OLS Regression Results
# ==============================================================================
# Dep. Variable:                  lwage   R-squared:                       0.235
# Model:                            OLS   Adj. R-squared:                  0.234
# Method:                 Least Squares   F-statistic:                     538.6
# Date:                Fri, 26 Jan 2024   Prob (F-statistic):               0.00
# Time:                        00:54:28   Log-Likelihood:                -11809.
# No. Observations:               26334   AIC:                         2.365e+04
# Df Residuals:                   26318   BIC:                         2.378e+04
# Df Model:                          15
# Covariance Type:            nonrobust
# =================================================================================================
#                                     coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------------------------
# Intercept                         6.7898      0.007    980.575      0.000       6.776       6.803
# tenure                            0.0029      0.000     25.683      0.000       0.003       0.003
# tenure_sqrd                   -5.579e-06   4.66e-07    -11.982      0.000   -6.49e-06   -4.67e-06
# bac                               1.0879      0.007    156.678      0.000       1.074       1.101
# more_than_bac                     1.3046      0.011    120.582      0.000       1.283       1.326
# secondaire                        0.8821      0.009    100.675      0.000       0.865       0.899
# partial_post_secondaire           0.8930      0.015     61.115      0.000       0.864       0.922
# post_secondaire                   1.0545      0.007    143.397      0.000       1.040       1.069
# no_secondaire                     0.8331      0.014     59.241      0.000       0.806       0.861
# none                              0.7346      0.028     26.530      0.000       0.680       0.789
# femme                            -0.0054      0.008     -0.655      0.512      -0.022       0.011
# bac_femme                         0.0698      0.011      6.131      0.000       0.047       0.092
# more_than_bac_femme              -0.0778      0.015     -5.192      0.000      -0.107      -0.048
# secondaire_femme                 -0.1843      0.013    -13.875      0.000      -0.210      -0.158
# partial_post_secondaire_femme    -0.1178      0.022     -5.336      0.000      -0.161      -0.075
# post_secondaire_femme            -0.2078      0.010    -19.870      0.000      -0.228      -0.187
# no_secondaire_femme              -0.2189      0.025     -8.887      0.000      -0.267      -0.171
# none_femme                       -0.2169      0.049     -4.431      0.000      -0.313      -0.121
# ==============================================================================
# Omnibus:                      139.360   Durbin-Watson:                   2.001
# Prob(Omnibus):                  0.000   Jarque-Bera (JB):              195.587
# Skew:                          -0.046   Prob(JB):                     3.38e-43
# Kurtosis:                       3.412   Cond. No.                     1.33e+19
# ==============================================================================
# #--------------------------------------------

#reponse question 3 #3 et #4: le coef de bac est de 1.0879 et le coef de none est de 0.7346 donce la difference en pourcentage du salaire pour un homme qui a un bac versus un homme qui a le plus petit niveau deducation est donc de 1.0879-0.7346 = 0.3533, donc en % on a une augmentation de 35.33% du salaire. pour une femme qui a un bac (bac_femme) versus une femme qui a le plus petit niveau deducation (none_femme) la difference en pourcentage du salaire est de 0.0698--0.2169 => 0.0698+0.2169 = 0.2867, donc en % on a une augmentation de 28.67% du salaire.

# reponse question 3 #5: soit le  model2 (lwage = b0 + b1(tenure) + b2(tenure_sqrd) + ... + b9(femme)), si on derrive par wage on a Dlwage/DU = b1 + 2b2(tenure) -> CPO -> 0 = b1 + 2 (b2)(tenure) -> -b1 = 2 (b2)(tenure) -> -b1/(2 (b2)) = tenure
#donc tenure = -0.0029 / 2 (-5.616e-06) = 258.9