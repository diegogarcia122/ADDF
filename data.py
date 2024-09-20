import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('top50.csv', encoding='utf-8', encoding_errors='replace')
print(df.head())
print('\n')
print(df.info())

numvalues = df.select_dtypes(np.number)

#
print('media')
print(numvalues.median())
print('\n')
print('mediana')
print(numvalues.mean())
print('\n')
print('moda')
print(numvalues.mode())
print('\n')
print('desviacion estandar')
print(numvalues.std())
print('\n')

for i in range(11):
    df_freq = pd.crosstab(numvalues.iloc[:,i], columns='count')
    print(df_freq.head())
    print('\n')


print('\n')

plt.hist(df['Beats.Per.Minute'], edgecolor='black')
plt.show()
plt.hist(df['Loudness..dB..'], edgecolor='black')
plt.show()

sns.heatmap(data = numvalues) 
plt.show()

sns.boxplot(df['Popularity'])
plt.show()

sns.boxplot(df['Liveness'])
plt.show()

sns.boxplot(df['Acousticness..'])
plt.show()

