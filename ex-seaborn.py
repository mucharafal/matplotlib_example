#%%[markdown]
# ## Introduction to data exploration & visualization

#%%[markdown]
# ### Tools:
#  1. **Pandas** - data analysis and manipulation
#  1. **Seaborn** - high-level data visualization
#  1. **Matplotlib** - data visualization

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%[markdown]
# ### How to get your data? 
# Pandas provides plenty of I/O methods
#
# https://pandas.pydata.org/pandas-docs/stable/reference/io.html 

# ### Penguins
# Preloaded dataset from seaborn
# 
# #### 1. Basic exploration

#%%
penguins = sns.load_dataset("penguins")

#%%
penguins.head()

#%%
penguins = penguins.dropna()
penguins.head()

#%%
penguins.describe()

#%%
g = sns.relplot(
    kind="scatter",
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="body_mass_g",
    style="species",
    palette="viridis_r")

g.fig.suptitle("Penguin weigth and bill dimmensions")

#%%
g = sns.relplot(
    kind="scatter",
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="body_mass_g",
    col="species",
    style="sex",
    col_wrap=2,
    palette="viridis_r"
)
g.fig.suptitle("Penguin weigth and bill dimmensions +")
plt.subplots_adjust(top=0.9)

#%%
g = sns.jointplot(data=penguins,
    x="flipper_length_mm",
    y="bill_length_mm",
    hue="species",
    palette="viridis_r")

g.fig.suptitle("Penguin flipper and bill sizes")
plt.subplots_adjust(top=0.9)

#%%[markdown]
# ### Good to know
# * **possibilities are unlimited** https://seaborn.pydata.org/examples/index.html
# * **colors matter** https://seaborn.pydata.org/tutorial/color_palettes.html
