import plotly.express as px
import csv
import numpy as np

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="sleep in hours", y="Coffee in ml")
        fig.show()

def getDataSource(dataPath):
    coffeeInML = []
    sleepInHours = []
    with open(dataPath) as csvFile:
        csv_reader = csv.DictReader(csvFile)
        for i in csv_reader:
            coffeeInML.append(float(i["Coffee in ml"]))
            sleepInHours.append(float(i["sleep in hours"]))

    return {"x" : coffeeInML, "y" : sleepInHours}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation is = ", correlation[0, 1])
    
def main():
    datapath = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)
    plotGraph(datapath)

main()        