import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('.\\DataSets\\niftyJoinedCloses.csv')
df_corr = df.corr()
print(df_corr.head())

data = df_corr.values
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
heatmap =  ax.pcolor(data)
fig.colorbar(heatmap)

ax.set_xticks(np.arange(data.shape[0])+0.5, minor = False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor = False)
ax.invert_yaxis()
ax.xaxis.tick_top()

column_labels = df_corr.columns
row_labels = df_corr.index

ax.set_xticklabels(column_labels)
ax.set_yticklabels(row_labels)
plt.xticks(rotation = 90)
heatmap.set_clim(-1,1)
plt.tight_layout()
plt.show()