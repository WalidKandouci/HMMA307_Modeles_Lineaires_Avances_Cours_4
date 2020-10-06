# Import Packages
%matplotlib notebook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from download import download
import seaborn as sns
import os
import statsmodels.api as sm
from statsmodels.formula.api import ols

sns.set_palette("colorblind")
url = "josephsalmon.eu/enseignement/datasets/Donnees_Comptages_Velos_Totem_Albert_1er_verbose.csv"

script_dir = os.path.abspath("")

download(url, script_dir, replace=False)
Totem = pd.read_csv("Donnees_Comptages_Velos_Totem_Albert_1er_verbose.csv", header=1)
Totem = Totem[Totem.columns[0:4]]
Totem.dropna(inplace=True)
Totem.columns = ["date", "time", "GTotal", "TTotal"]
Totem.head()
Totem.describe()
Totem.info()
Totem['GTotal'] = [float(str(val).replace(' ','').replace(',','.').replace("\u202f", "")) for val in Totem['GTotal'].values]
Totem['TTotal'] = [float(str(val).replace(' ','').replace(',','.').replace("\u202f", "")) for val in Totem['TTotal'].values]
Totem.head()
Totem['date_time'] = Totem['date'].astype(str) + ' ' + Totem['time']
Totem['date_time'] = pd.to_datetime(Totem.date_time)
Totem.dtypes
Totem
Totem.set_index('date_time', inplace=True)
Totem.head()
pd.to_datetime(Totem.index)
Totem['months'] = Totem.index.month
Totem.head()
calend_mth = {1:'Jan', 2:'Feb', 3:'March', 4:'Apr', 5:"May", 6:"Jun",7:"July",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
Totem.replace({'months': calend_mth}, inplace=True)
sns.violinplot(x="months", y='GTotal', data=Totem)
