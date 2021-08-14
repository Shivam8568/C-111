import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics as st
import random 
import pandas as pd 
import csv 
df = pd.read_csv("Data1.csv")
data = df["score"].tolist()
def randomsetofmean(counter):
    dataset = []    
    for i in range (0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
def show_fig(meanlist):
    df = meanlist
    mean = st.mean(df)
    fig = ff.create_distplot([df],["score"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = (0,1),mode = "lines", name = "Mean"))
    fig.show()
def setup():
    meanlist = []
    for i in range (0,1000):
        setofmean = randomsetofmean(100)
        meanlist.append(setofmean)
        show_fig(meanlist)
        mean = st.mean(meanlist)
        print(mean)
setup()



