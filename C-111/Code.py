import csv 

import statistics as st
import plotly.figure_factory as ff
import pandas as pd 
df = pd.read_csv("Data1.csv")
data = df["score"].tolist()
fig = ff.create_distplot([data],["score"],show_hist=False)
#fig.show()
mean = st.mean(data)
sd = st.stdev(data)
print (mean)
print (sd)