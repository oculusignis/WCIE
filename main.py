import requests

def timestamp():
    # in eine funktion
    import datetime as dt

    current_date_gtm = dt.datetime.utcnow()
    print(current_date_gtm)

    # current_date = dt.datetime.now()
    # print(current_date)

    string_date_start = current_date_gtm.strftime("%Y-%m-%d 00:00:00")
    print(string_date_start)
    string_date_end = current_date_gtm.strftime("%Y-%m-%d 21:00:00")
    print(string_date_end)

    date_object_start = dt.datetime.strptime(string_date_start, "%Y-%m-%d %H:%M:%S")
    print(date_object_start)
    date_object_end = dt.datetime.strptime(string_date_end, "%Y-%m-%d %H:%M:%S")
    print(date_object_end)

    millisecstart = round(date_object_start.timestamp() * 1000)
    print(millisecstart)
    millisecend = round(date_object_end.timestamp() * 1000)
    print(millisecend)

    return millisecstart, millisecend


##API URL
url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
r = requests.get(url)
string = r.content.decode("utf-8")

print(string)
print(string[5])  # me like <- git test
