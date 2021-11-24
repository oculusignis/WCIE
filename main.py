import requests

# dict with the location name as keys and the swiss1903 coordinates as values
locations = {"Rapperswil OST Campus": (704301, 231052),
             "Rapperswil Seebad": (704077, 231654),
             "Schmerikon Badi": (714163, 231433),
             "Insel Lützelau Nordost": (703019, 23235),
             "Zürich Seebad Utoquai": (683598, 246245),
             "Strandbad Meilen": (691516, 235727),
             "Lachen SZ": (706947, 228423),
             "Noulen SZ": (709651, 229673)
             }


def templist(url):
    """converts the url response to a list containing only the temperatures"""
    # get the data and save as string
    data_string = requests.get(url).content.decode("utf8")
    # convert string to list and remove first element representing depth
    data_list = data_string[data_string.find("\n")+1:].split(",")
    data_list.pop(0)
    # convert strings in list to float
    float_list = [float(x) for x in data_list]
    return float_list


def datadict():
    testtime = 1637762400000
    # TODO francos time function should deliver time1, time2
    time1 = testtime
    time2 = testtime
    data = {}
    for key in locations.keys():
        x, y = locations[key]
        loc_url = f"http://meteolakes.ch/api/coordinates/{x}/{y}/zurich/temperature/{time1}/{time2}/1"
        data[key] = templist(loc_url)
        print(data[key])
    return data


def fileScanner():
    """Returns a dictionary with location name as key and a string of water temperatures as value.
    Locations and values read in from text file "tempData.txt" """
    dataDict = dict()
    maxsplit = 1
    with open("tempData.txt") as file:
        for line in file:                                   # iteration line by line
            dataString = line.rstrip()                      # reads line into string
            dataList = dataString.split(",", maxsplit)      # splits string into 2 substrings after first comma
            dataDict[dataList[0]] = dataList[1]             # adds element to dictionary: 1. substring as key, 2. substring as value
    return dataDict


# API URL
testurl = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
temp_list = templist(testurl)
print(temp_list)
print("\n\n")
print(datadict())
