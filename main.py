import requests

def fileScanner():
    """Returns a dictionary with location name as key and a string of water temperatures as value.
    Locations and values read in from text file "tempData.txt" """
    dataDict = dict()
    maxsplit = 1
    with open("tempData.txt") as file:
        for line in file:                                   #iteration line by line
            dataString = line.rstrip()                      #reads line into string
            dataList = dataString.split(",", maxsplit)      #splits string into 2 substrings after first comma
            dataDict[dataList[0]] = dataList[1]             #adds element to dictionary: 1. substring as key, 2. substring as value
    return dataDict

print(fileScanner())

##API URL
url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1637478000000/1637485200000/1"
r = requests.get(url)
string = r.content.decode("utf-8")
print(string)








