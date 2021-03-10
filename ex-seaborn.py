#%%[markdown]
# # Introduction to data exploration & visualization

#%%[markdown]
# ## Tools:
#  1. **Pandas** - data analysis and manipulation
#  1. **Seaborn** - high-level data visualization
#  1. **Matplotlib** - data visualization

#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#%%[markdown]
# ## How to get your data? 
# Pandas provides plenty of I/O methods
#
# https://pandas.pydata.org/pandas-docs/stable/reference/io.html 

# ## Penguins
# Preloaded dataset from seaborn
# 
# ### 1. Basic data exploration

#%%
penguins = sns.load_dataset("penguins")

#%%
penguins.head()

#%%
penguins = penguins.dropna()
penguins.head()

#%%
penguins.describe()

#%%[markdown]
# ### 2. Visualization
# #### Basic chart

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

#%%[markdown]
# #### More detailed chart

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

#%%[markdown]
# #### Multi-chart

#%%
g = sns.jointplot(data=penguins,
    x="flipper_length_mm",
    y="bill_length_mm",
    hue="species",
    palette="viridis_r")

g.fig.suptitle("Penguin flipper and bill sizes")
plt.subplots_adjust(top=0.9)

#%%[markdown]
# ## Custom charts
# ## CERN - Alice measurements

#%%
df_min = pd.read_csv("2m_insertedobjects_min", sep="\t", header=None)
df_min.columns = ["rectime", "id", "mval", "mmin", "mmax"]
df_min.rectime = df_min.rectime.apply(lambda timestamp: datetime.datetime.fromtimestamp(timestamp))

alicdb1_min = df_min[df_min.id == 4]
alicdb2_min = df_min[df_min.id == 11]

df_avg = pd.read_csv("2m_insertedobjects_r", sep="\t", header=None)
df_avg.columns = ["rectime", "id", "mval", "mmin", "mmax"]
df_avg.rectime = df_avg.rectime.apply(lambda timestamp: datetime.datetime.fromtimestamp(timestamp))

alicdb1_avg = df_avg[df_avg.id == 2]
alicdb2_avg = df_avg[df_avg.id == 9]

#%%
alicdb2_avg.head()

#%%[markdown]
# #### Basic chart

#%%
alicdb2_min.plot.line(x="rectime", y = "mmin")
alicdb2_avg.plot.line(x="rectime", y = "mval")

#%%[markdown]
# #### Issues?
# * Missing titles
# * Two separate charts describing same data
# * Axis missing description and/or units
# * Missing grid
# * Missing end of range data ticks (axis Y chart 1)
# * Unnecessary whitespace on the left and right sides
# * Meaningless legend names

#%%[markdown]
# #### Solution:

#%%
ax = alicdb2_min.plot.line(
    x="rectime", y = "mmin", # dane
    title="alicdb2\n minimal and average insert rate", 
    c="r", # kolor
    label = "min value") # nazwa w legendzie
alicdb2_avg.plot.line(x="rectime", y = "mval", ax = ax, label = "avg value")

ax.set_xlabel("Time") # Podpisanie osi
ax.set_ylabel("Insert rate [Hz]")

plt.grid(True, which="major", axis="both")  # siatka

ax.set_yticks([188, 190, 192, 194, 196, 198, 200, 202])  # wartości na siatce, czasem warto wprowadzić ręcznie

ax.set_xlim(alicdb2_min.rectime.min(), alicdb2_min.rectime.max()) # a czasem wystarczy je sensownie ograniczyć

# plt.savefig("minimal_and_avg_insert_rate_alicdb2.png")  # można zapisać do pliku


#%%[markdown]
# #### Advanced Solution:

#%%
ax = alicdb2_min.plot.scatter(
    x="rectime", y = "mmin", 
    title=r"$\alpha$licd$\beta^{2}$" + "\n minimal and average insert rate",   # tex notation in titles
    c="r", 
    marker=".",
    s = (alicdb2_min.mmin - 188) * 4)
alicdb2_min.plot.line(
    x="rectime", 
    y = "mmin", 
    ax = ax, 
    c="r", 
    label = "min value")
alicdb2_avg.plot.line(x="rectime", y = "mval", ax = ax, label = "avg value", linewidth = 5)

ax.set_xlabel("Time")
ax.set_ylabel("Insert rate [Hz]")

plt.grid(True, which="major", axis="both")

ax.set_yticks([188, 190, 192, 194, 196, 198, 200, 202])

ax.set_xlim(alicdb2_min.rectime.min(), alicdb2_min.rectime.max())

plt.savefig("minimal_and_avg_insert_rate_alicdb2.png")

#%%[markdown]
# ## Good to know
# * **possibilities are unlimited** https://seaborn.pydata.org/examples/index.html
# * **colors matter** https://seaborn.pydata.org/tutorial/color_palettes.html
