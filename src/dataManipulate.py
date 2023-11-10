import csv
import datetime
import os

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DATA_FOLDER = os.path.join(root_path, 'data/')

def writeCsv(dataList):
  csvName = "data-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + ".csv"
  
  with open(DATA_FOLDER + csvName, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    header = dataList[0].keys()
    writer.writerow(header)
        
    for row in dataList:
        writer.writerow(row.values())