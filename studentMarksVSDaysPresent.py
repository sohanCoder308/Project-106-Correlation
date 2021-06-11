import plotly.express as px
import csv
import numpy as np

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(dataPath):
    marksInPercentage = []
    daysPresent = []
    with open(dataPath) as csvFile:
        csv_reader = csv.DictReader(csvFile)
        for i in csv_reader:
            marksInPercentage.append(float(i["Marks In Percentage"]))
            daysPresent.append(float(i["Days Present"]))

    return {"x" : marksInPercentage, "y" : daysPresent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation is = ", correlation[0, 1])
    
def main():
    datapath = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
    plotGraph(datapath)

main()        