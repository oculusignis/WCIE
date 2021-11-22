import requests

def timestamp():

    import datetime as dt
    # get the current GTM time zone date and time
    current_date_gtm = dt.datetime.utcnow()

    # get the current local time zone date and time (for future use)
    # current_date = dt.datetime.now()

    # convert current GTM date to string with current time at 00:00:00
    string_date_start = current_date_gtm.strftime("%Y-%m-%d 00:00:00")
    # convert current GTM date to string with current time at 21:00:00
    string_date_end = current_date_gtm.strftime("%Y-%m-%d 21:00:00")

    #convert day start string into object
    date_object_start = dt.datetime.strptime(string_date_start, "%Y-%m-%d %H:%M:%S")
    # convert day end string into object
    date_object_end = dt.datetime.strptime(string_date_end, "%Y-%m-%d %H:%M:%S")

    #Multiply the timestamp of the datetime object day start by 1'000 to convert into millisec and round to remove .0
    millisecstart = round(date_object_start.timestamp() * 1000)
    # Multiply the timestamp of the datetime object day end by 1'000 to convert into millisec and round to remove .0
    millisecend = round(date_object_end.timestamp() * 1000)

    return millisecstart, millisecend


##API URL
url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
r = requests.get(url)
string = r.content.decode("utf-8")

print(string)
print(string[5])  # me like <- git test
