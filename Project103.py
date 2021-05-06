import pandas as pd
import csv
import plotly.express as pe

df = pd.read_csv("Project103Data.csv")
fig = pe.scatter(df,x="date",y="cases",color="country")

fig.show()