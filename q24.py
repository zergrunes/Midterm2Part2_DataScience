import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = [32, 13, 19, 37, 27, 22, 20, 87, 42, 14, 26, 28, 35, 31, 10]
df = pd.DataFrame({'data': data})
sns.boxplot(data=df, orient='h', showmeans=True,
            palette='Set2')
plt.show()
print('\n Getting information...')
print('Mean:', df.mean())
print('Median:', df.median())
print('8 Quantiles:', pd.qcut(df.data, q=8))
print('Q1', df.quantile(q=.25))
print('Q3', df.quantile(q=.75))
print('IQR', [df.quantile(q=.75)-df.quantile(q=.25)])
print('Upper:', [df.quantile(q=.75)+(1.5*14.0)])
print('Lower:', [df.quantile(q=.25)-(1.5*14.0)])
