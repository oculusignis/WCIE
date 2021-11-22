import requests

def savetofile (dataDictionary):
    with open('tempData.txt', 'w') as f:
        for key, value in dataDictionary.items():
            f.write(str(key) + "," + str(value) + "\n")

