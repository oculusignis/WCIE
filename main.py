## @package main
#  \brief     Shows Temperature-data around the Zurich See
#  \author    Marc Lippuner
#  \author    Franco Caminada
#  \author    Gian Luca Brazerol
#  \author    Luca Brügger
#  \date      13.12.2021
#  \bug       none
#  \copyright GNU Public License.

import requests
import datetime
import os

## \fn templist(url)
# \param url The url as a String.

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

## \fn datadict()

def datadict():
    """creates dictionary with current temperature-data for each location"""
    time1, time2 = timestamp()
    data = {}
    locations = location_scanner()
    for key in locations.keys():
        x, y = locations[key]
        loc_url = f"http://meteolakes.ch/api/coordinates/{x}/{y}/zurich/temperature/{time1}/{time2}/1"
        data[key] = templist(loc_url)

    return data

## \fn file_scanner()

def file_scanner():
    """Returns a dictionary with location name as key and a string of water temperatures as value.
    Locations and values read in from text file 'tempData.txt'"""
    data_dict = dict()
    with open("tempData.txt", encoding="utf-8") as file:
        for line in file:                             # iteration line by line
            data_string = line.rstrip()               # reads line into string
            data_list = data_string.split(",")        # splits string into substrings after every comma
            data_dict[data_list[0]] = list(float(x) for x in data_list[1:-1])  # adds element to dictionary:
            # first substring as key, others as float numbers
    return data_dict

## \fn location_scanner()

def location_scanner():
    """Returns a dictionary with location name as key and a tuple of int (X and Y coordinates) as value.
    Locations and values read in from text file "locations.txt" """
    location_dict = dict()
    with open("locations.txt", encoding="utf-8") as file:
        for line in file:                           # iteration line by line
            data_string = line.rstrip()             # reads line into string
            data_list = data_string.split(",")      # splits string into substrings after every comma
            location_dict[data_list[0]] = (int(data_list[1]), int(data_list[2]))    # adds element to dictionary:
            # first substring as key, 2nd and 3rd string as value (int tuple)
    return location_dict

## \fn dict_printer(data_dict)
# \param data_dict The Dictionary.

def dict_printer(data_dict):
    """Takes a dictionary and prints it to the console: Location: Value (actual time)"""
    for key in data_dict:
        print(f"{key+':':<25} {data_dict[key][int(datetime.datetime.now().hour/3)]:>.1f} °C")

## \fn timestamp()

def timestamp():
    """converts current date start and date at 9pm into two epoch time stamps"""
    # get the current local time zone date and time (for future use)
    current_datetime = datetime.datetime.now()

    # convert current date to string with time at 00:00:00
    string_date_start = current_datetime.strftime("%Y-%m-%d 00:00:00")
    # convert current date to string with time at 23:59:00
    string_date_end = current_datetime.strftime("%Y-%m-%d 23:59:00")

    # convert day start string into object
    date_object_start = datetime.datetime.strptime(string_date_start, "%Y-%m-%d %H:%M:%S")
    # convert day end string into object
    date_object_end = datetime.datetime.strptime(string_date_end, "%Y-%m-%d %H:%M:%S")

    # Multiply the timestamp of the datetime object day start by 1'000 to convert into millisec and round to remove .0
    millisecstart = round(date_object_start.timestamp() * 1000)
    # Multiply the timestamp of the datetime object day end by 1'000 to convert into millisec and round to remove .0
    millisecend = round(date_object_end.timestamp() * 1000)

    return millisecstart, millisecend

## \fn datecomparison()

def datecomparison():
    """read last modified date of file and compare it to current date, returns bool"""
    if not os.path.exists("tempData.txt"):
        return False
    # get epoch time of last file modification of file
    filedate_epoch = os.path.getmtime("tempData.txt")
    # convert epoch time to normal time
    full_filedate = datetime.datetime.fromtimestamp(filedate_epoch)
    # convert time into string,take away H-M-S and leave date alone
    filedate = full_filedate.strftime("%Y-%m-%d")

    # give current date
    current_date = datetime.date.today()
    # convert current date object to string
    string_current_date = current_date.strftime("%Y-%m-%d")
    # return true if current date and filedate are the same
    return string_current_date == filedate


## \fn savetofile(dataDictionary)
# \param dataDictionary The Dictionary.

def savetofile(dataDictionary):
    """save dictionary to file line per line (key and value separated by comma)"""
    with open('tempData.txt', 'w', encoding='utf-8') as f:
        for key, value in dataDictionary.items():
            newval = str(value)
            newval = newval.replace("[", "")
            newval = newval.replace("]", "")
            f.write(str(key) + "," + newval + "\n")


# program execution
if datecomparison():
    ## \var location_temps
    # contains all the data needed in a Dictionary
    location_temps = file_scanner()
else:
    location_temps = datadict()
    savetofile(location_temps)

dict_printer(location_temps)
