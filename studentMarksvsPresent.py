import csv
import plotly.express as pe
import numpy as np
def plotFigure(dataPath):
    with open(dataPath)as f:
        df= csv.DictReader(f)
        fig=pe.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()
def getDataSource(dataPath):
    marks=[]
    days=[]
    with open(dataPath)as f:
        df= csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x" : marks,"y":days}
def getCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
def setup():
    dataPath="./Student Marks vs Days Present.csv"
    dataSource=getDataSource(dataPath)
    getCorrelation(dataSource)
    plotFigure(dataPath)
setup()