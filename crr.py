import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# arr = 'пол,возраст,факультет,соцсети,видео,игры,фото видео,списывание,чтение,частота покупок,экран,камера,автономность,производительность,бренд'.split(',')

df = pd.read_csv('data2.csv')

# for e in arr:
#     print('\n'.join(str(df.groupby(e)['N'].count()).split('\n')[:-1]))
#
# df = df.drop('N', axis=1)



corr = df.corr()
sns.heatmap(corr, cmap="Greens", annot=True)
plt.show()
