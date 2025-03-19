import pandas as pd;
import numpy as np;
import sklearn as sk;
import xgboost as xgb;
import matplotlib as plt;
import seaborn as sns;

df = pd.read_csv(r'C:\datosTFG\Carpeta tocha de prestamos 07-18\accepted_2007_to_2018q4.csv\accepted_2007_to_2018Q4.csv')
df.head()