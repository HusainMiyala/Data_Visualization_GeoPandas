import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("J:/APc_plan/Control Group/ALC/ALC TM's/Husain M/Projects/SolarOutput_Province.csv")

map_df = gpd.read_file("J:/APc_plan/Control Group/ALC/ALC TM's/Husain M/Projects/lpr_000b16a_e.shp")
map_df = map_df.rename({'PRENAME':'Province'}, axis = 'columns')
map_df = map_df.drop(['PRUID', 'PRNAME', 'PRFNAME', 'PREABBR', 'PRFABBR'], axis = 1)

df_merge = map_df.merge(df, left_on =['Province'], right_on =['Province'])
#print(df_merge)

fig, ax = plt.subplots(1, figsize=(12,12))
plt.title('Solar Power Generated in Canada (Oct 2020 - Oct 2021)')
df_merge.plot(column="Oct '20 - Oct '21", cmap='OrRd', linewidth=1, ax=ax, edgecolor='0.9', legend = True, legend_kwds = {'label':'Megawatt Hours (in 100K)'})
ax.axis('off')

plt.show()
