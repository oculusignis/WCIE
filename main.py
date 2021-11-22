import requests

## Function to save a Dictionary
# The Dictionary will be saved line per line 
# with the key and the value separated by a comma.
def savetofile (dataDictionary):
    """save dictionary to file line per line (key and value separated by comma)"""
    with open('tempData.txt', 'w') as f:
        for key, value in dataDictionary.items():
            f.write(str(key) + "," + str(value) + "\n")
