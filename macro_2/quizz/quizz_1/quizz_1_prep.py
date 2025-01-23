import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("macro_2/quizz/quizz_1/data/Quiz1.xls")
print(df.head())
# print all columns from df
print(df.columns)
df_cyc = df[['Time', "GDP_cyc", "C_cyc", "EXP_cyc", "I_cyc", "IMP_cyc", "G_cyc"]]
# compute the correlation matrix of df_cyc and plot it using matplotlib
correlation = df_cyc.corr()
# print(correlation)
plt.imshow(correlation, cmap='viridis', interpolation='none')
plt.colorbar()

# Set the labels for the x and y axes
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)

# Add text annotations for the correlation coefficients
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(j, i, f'{correlation.iloc[i, j]:.2f}', ha='center', va='center', color='white')

# plt.show()
# print the correlation coef of EXP_cyc and GDP_cyc
print(correlation["EXP_cyc"]["GDP_cyc"])
print(correlation["IMP_cyc"]["GDP_cyc"])
print(correlation["I_cyc"]["GDP_cyc"])

for column in df_cyc.columns:
    print(f"Column {column} has a standard deviation of {df_cyc[column].std()}")

df_question1 = df[["GDP", "EXP"]]
df_question1["exp_prop"] = df_question1["EXP"] / df_question1["GDP"]
# can we average the column "exp_prop"?
# print(df_question1["exp_prop"].mean())

question2 = df[["GDP", "EXP", "IMP"]]
question2["imp_exp"] = (question2["EXP"] - question2["IMP"]) / question2["GDP"]
# print(question2["imp_exp"].mean())

question3 = df[["Time", "GDP", "IMP"]]
question3["imp_prop"] = question3["IMP"] / question3["GDP"]
# filter to only keep last record
question3a = question3[question3["Time"] == question3["Time"].max()]
question3b = question3[question3["Time"] == question3["Time"].min()]
# print(question3a.head())
# print(question3b.head())



question4 = df[["Time", "GDP", "G"]]
question4["G_prop"] = question4["G"] / question4["GDP"]
question4a = question4[question4["Time"] == question4["Time"].max()]
question4b = question4[question4["Time"] == question4["Time"].min()]

# print(question4a.head())
# print(question4b.head())

question5 = df[["GDP", "G"]]
question5["g_prop"] = question5["G"] / question5["GDP"]
print(question5["g_prop"].mean())


question6 = df[["Time", "GDP", "C"]]
question6["G_prop"] = question6["C"] / question6["GDP"]
question6a = question6[question6["Time"] == question6["Time"].max()]
question6b = question6[question6["Time"] == question6["Time"].min()]

print(question6a.head())
print(question6b.head())


question7 = df[["Time", "GDP", "I"]]
question7["G_prop"] = question7["I"] / question7["GDP"]
question7a = question7[question7["Time"] == question7["Time"].max()]
question7b = question7[question7["Time"] == question7["Time"].min()]

print(question7a.head())
print(question7b.head())

question8 = df[["GDP", "I"]]
question8["g_prop"] = question8["I"] / question8["GDP"]
print(question8["g_prop"].mean())