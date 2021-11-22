import requests

def savetofile (dataList):
    with open('tempData.txt', 'w') as f:
        for item in dataList:
            f.write("%s\n" % item)



##API URL
#url = "http://meteolakes.ch/api/coordinates/534700/144950/geneva/temperature/1537034400000/1537768800000/20"
#r = requests.get(url)
#string = r.content.decode("utf-8")

#print(string)
#print(string[5])  # me like <- git test

#savetofile(string)

my_list = [1, 2, 3]
savetofile(my_list)
