import requests


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


##API URL
url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
temp_list = templist(url)
print(temp_list)
