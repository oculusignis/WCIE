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


def datadict():
    testtime = 1637762400000
    time1, time2 = timestamp()
    data = {}
    for key in locations.keys():
        x, y = locations[key]
        loc_url = f"http://meteolakes.ch/api/coordinates/{x}/{y}/zurich/temperature/{time1}/{time2}/1"
        data[key] = templist(loc_url)
    return data


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

def timestamp():
    # get the current GTM time zone date and time
    current_date_gtm = datetime.datetime.utcnow()

    # get the current local time zone date and time (for future use)
    # current_date = datetime.datetime.now()

    # convert current GTM date to string with current time at 00:00:00
    string_date_start = current_date_gtm.strftime("%Y-%m-%d 00:00:00")
    # convert current GTM date to string with current time at 21:00:00
    string_date_end = current_date_gtm.strftime("%Y-%m-%d 21:00:00")

    # convert day start string into object
    date_object_start = datetime.datetime.strptime(string_date_start, "%Y-%m-%d %H:%M:%S")
    # convert day end string into object
    date_object_end = datetime.datetime.strptime(string_date_end, "%Y-%m-%d %H:%M:%S")

    # Multiply the timestamp of the datetime object day start by 1'000 to convert into millisec and round to remove .0
    millisecstart = round(date_object_start.timestamp() * 1000)
    # Multiply the timestamp of the datetime object day end by 1'000 to convert into millisec and round to remove .0
    millisecend = round(date_object_end.timestamp() * 1000)

    return millisecstart, millisecend


## Function to save a Dictionary
# The Dictionary will be saved line per line 
# with the key and the value separated by a comma.
def savetofile(dataDictionary):
    """save dictionary to file line per line (key and value separated by comma)"""
    with open('tempData.txt', 'w') as f:
        for key, value in dataDictionary.items():
            newval = str(value)
            newval = newval.replace("[", "")
            newval = newval.replace("]", "")
            f.write(str(key) + "," + newval + "\n")


# API URL
print(datadict())
