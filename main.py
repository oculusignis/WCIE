import requests
import datetime


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


def file_scanner():
    """Returns a dictionary with location name as key and a string of water temperatures as value.
    Locations and values read in from text file "tempData.txt" """
    data_dict = dict()
    with open("tempData.txt") as file:
        for line in file:                             # iteration line by line
            data_string = line.rstrip()               # reads line into string
            data_list = data_string.split(",")        # splits string into substrings after every comma
            data_dict[data_list[0]] = list(float(x) for x in data_list[1:-1])  # adds element to dictionary:
            # 1. substring as key, others as float numbers
    return data_dict


def dict_printer(data_dict):
    """"Takes a dictionary and prints it to the console: Location: Value (actual time)"""
    for key in data_dict:
        print(f"{key+':':<25} {data_dict[key][int(datetime.datetime.now().hour/3)]:>}")


# API URL
testurl = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
temp_list = templist(testurl)
print(temp_list)
