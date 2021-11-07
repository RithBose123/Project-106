import csv
import plotly.express as pe
import numpy as np
def plotFigure(dataPath):
    with open(dataPath) as f:
        df=csv.DictReader(f)
        fig=pe.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()
def getDataSource(dataPath):
    coffee=[]
    sleep=[]
    with open(dataPath) as f:
        df=csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}
def getCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
def setup():
    dataPath="./cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(dataPath)
    getCorrelation(dataSource)
    plotFigure(dataPath)
setup()