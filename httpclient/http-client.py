import http.client as hc

connection  = hc.HTTPConnection("www.journaldev.com")
connection.request("GET","/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason)) # Status: 301 and reason: Moved Permanently
print(response.read().decode()) # get response body
