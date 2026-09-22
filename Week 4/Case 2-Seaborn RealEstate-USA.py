import seaborn as sns
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
sns.set_theme()

df=pd.read_csv(r'seaBorn\RealEstate-USA.csv',delimiter=',')
print(df.dtypes)

sns.lineplot(x='bed',y='price',data=df)
plt.show()
#input('wait for me......')

sns.lineplot(x='bed',y='bath',data=df)
plt.show()

sns.boxplot(x='price',y='city',data=df)
plt.show()

sns.catplot(x='bed',y='bath',data=df)
plt.show()

sns.barplot(x='price',y='bed',data=df,hue='city',)
plt.show()

dillfter=df.head(10)
g=sns.histplot(data=df,x='price',hue='bath',bins=20)
g.figure.suptitle('bed')
plt.show()


sns.barplot(data=df,x='bed',y='bath',hue='price')
plt.show()

sns.violinplot(data=df,x='status',y='bed',hue='bath',split=True,fill=False)
plt.show()

sns.violinplot(data=df,x='status',y='city',hue='street',split=True,fill=False)
plt.show()
