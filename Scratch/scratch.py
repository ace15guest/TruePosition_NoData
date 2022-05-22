import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec
import matplotlib.dates as mdates

facecolor = '#EAEAEA'
color_bars = '#3475D0'
txt_color1 = '#252525'
txt_color2 = '#004C74'

df = pd.read_csv('Space_Corrected.csv')
df['Datum'] = pd.to_datetime(df['Datum'], utc=True)
df['Rocket'] = pd.to_numeric(df[' Rocket'], errors='coerce')
df.drop([' Rocket', 'Unnamed: 0', 'Unnamed: 0.1'], axis=1, inplace=True)
facecolor = '#EAEAEA'
color_bars = '#3475D0'
txt_color1 = '#252525'
txt_color2 = '#004C74'
fig, ax = plt.subplots(1, figsize=(20,6), facecolor=facecolor)
ax.set_facecolor(facecolor)
n, bins, patches = plt.hist(df.Rocket, color=color_bars, bins='doane')
#grid
minor_locator = AutoMinorLocator(2)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.grid(which='minor', color=facecolor, lw = 0.5)
xticks = [(bins[idx+1] + value)/2 for idx, value in enumerate(bins[:-1])]
xticks_labels = [ "{:.0f}-{:.0f}".format(value, bins[idx+1]) for idx, value in enumerate(bins[:-1])]
plt.xticks(xticks, labels=xticks_labels, c=txt_color1, fontsize=13)
# remove major and minor ticks from the x axis, but keep the labels
ax.tick_params(axis='x', which='both',length=0)
# remove y ticks
plt.yticks([])
# Hide the right and top spines
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
for idx, value in enumerate(n):
    if value > 0:
        plt.text(xticks[idx], value+5, int(value), ha='center', fontsize=16, c=txt_color1)
plt.title('Histogram of Space Missions Costs\n', loc = 'left', fontsize = 20, c=txt_color1)
plt.xlabel('\nMillions of USD', c=txt_color2, fontsize=14)
plt.ylabel('Number of Space Missions', c=txt_color2, fontsize=14)
plt.tight_layout()
plt.savefig('costs.png', facecolor=facecolor)