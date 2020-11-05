import csv
import pandas as pnd
import plotly.express as px
from collections import Counter


with open('icecream.csv') as file:
    data = csv.DictReader(file)
    g = px.scatter(data, x = 'Temperature', y = 'Cold drink sales')
    g.show()


import csv
import numpy as np
import pandas as pnd
import plotly.express as px
from collections import Counter


def getData(dataPath):
    coldDrink = []
    temps = []
    with open(dataPath) as file:
        data = csv.DictReader(file)
        for i in data:
            coldDrink.append(float(i['Cold drink sales']))
            temps.append(float(i['Temperature']))
    return{"x" : temps, "y": coldDrink}
        
        
        #g = px.scatter(data, x = 'Temperature', y = 'Cold drink sales')
        #g.show()
        
def findCor(dataSource):
    cor = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation : ", cor[0, 1])
    
def main():
    dataPath = 'icecream.csv'
    dataSource = getData(dataPath)
    findCor(dataSource)
    
    
main()

import csv
import numpy as np
import pandas as pnd
import plotly.express as px
from collections import Counter


def getData(dataPath):
    coldDrink = []
    temps = []
    with open(dataPath) as file:
        data = csv.DictReader(file)
        for i in data:
            coldDrink.append(float(i['Size of TV']))
            temps.append(float(i['Average time']))
    return{"x" : temps, "y": coldDrink}
        
        
        
def findCor(dataSource):
    cor = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation : ", cor[0, 1])
    
def main():
    dataPath = 'tv-screen.csv'
    dataSource = getData(dataPath)
    findCor(dataSource)
    
with open('tv-screen.csv') as file:
    data = csv.DictReader(file)
    g = px.scatter(data, x = 'Size of TV', y = 'Average time')
    g.show()
    
main()

import csv
import numpy as np
import pandas as pnd
import plotly.express as px
from collections import Counter


def getData(dataPath):
    coldDrink = []
    temps = []
    with open(dataPath) as file:
        data = csv.DictReader(file)
        for i in data:
            coldDrink.append(float(i['Marks In Percentage']))
            temps.append(float(i['Days Present']))
    return{"x" : temps, "y": coldDrink}
        
        
        
def findCor(dataSource):
    cor = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation : ", cor[0, 1])
    
def main():
    dataPath = 'studentsmarks.csv'
    dataSource = getData(dataPath)
    findCor(dataSource)
    
with open('studentsmarks.csv') as file:
    data = csv.DictReader(file)
    g = px.scatter(data, x = 'Days Present', y = 'Marks In Percentage')
    g.show()
    
main()
