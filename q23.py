import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# hexbin plot
n = 10000
df2 = pd.DataFrame({'x': np.random.randn(n),
                   'y': np.random.rand(n)})
hexbin_plot = df2.plot.hexbin(x='x', y='y', gridsize=20)
plt.show()
# stacked bar chart
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)
stacked = df.plot.bar(stacked=True, color={
                      "speed": "yellow", "lifespan": "red"})
plt.show()
# pie plot
df3 = pd.DataFrame({'diameter': [4879.4, 12103.6, 12756.3, 6794.4],
                    'mass': [.330, 4.87, 5.97, 6.42]},
                   index=['Mercury', 'Venus', 'Earth', 'Mars'])
pie = df3.plot.pie(y='mass', figsize=(5, 5))
plt.show()
# area plot
df4 = pd.DataFrame({
    'sales': [3, 2, 3, 9, 10, 6],
    'signups': [5, 5, 6, 12, 14, 13],
    'visits': [20, 42, 28, 62, 81, 50],
}, index=pd.date_range(start='2018/01/01', end='2018/07/01',
                       freq='M'))
area = df.plot.area(stacked=False)
plt.show()
# scatter plot
df5 = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                   [6.4, 3.2, 1], [5.9, 3.0, 2]],
                   columns=['length', 'width', 'species'])
scatter = df5.plot.scatter(x='length',
                           y='width',
                           c='species',
                           colormap='viridis')
plt.show()
# box plot
np.random.seed(4323)
df6 = pd.DataFrame(np.random.randn(10, 4),
                   columns=['A', 'B', 'C', 'D'])
boxplot = df6.boxplot(column=['A', 'B', 'C', 'D'])
plt.show()
# plot multiple data columns
np.random.seed(0)
numbers = [["New York", 8.6, 20],
           ["Chicago", 2.7, 20],
           ["Los Angeles", 3.9, 20]]
df7 = pd.DataFrame(numbers, columns=[
                   "City", "Population(million)", "Year(2020)"])
df7.plot(x="City", y=["Population(million)", "Year(2020)"],
         kind="line", figsize=(10, 10))
plt.show()
# customized box plot
custom = pd.DataFrame(np.random.randn(10, 5),
                      columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5'])
boxplot = custom.boxplot(column=['Col1', 'Col2', 'Col4'])
plt.show()
