##Author: Jesse Lewis##
##Date: 24FEB21##

##NX-API Sandbox##


####Imports that need to be on to use APIs
import requests
import json

"""
Be sure to run feature nxapi first on Nexus Switch

"""

###API call paramaters that are passed back to the website.
switchuser='cisco'
switchpassword='cisco'

url='https://10.10.20.177/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1
    },
    "id": 1
  }
]

'''

verify=False below is to accept untrusted certificate
'''

###What arguments are received back into variable response
###This pulls back the show version in response variable
response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()


###Version 1

###Set variables for the switch hostname, memory and memory type
memory = str(response["result"]["body"]["memory"])
host = response["result"]["body"]["host_name"]
memType = response["result"]["body"]["mem_type"]

###Prints out the results
print("Version 1")
print("Hostname = " + host + "\t" + "Memory = " + memory + " " + memType)

print("\r")
###Version 2
### No variables and pulls information directly from the dictonary and keys
print("Version 2")
print("Hostname = " + response["result"]["body"]["host_name"] + "\t" + "Memory = " + str(response["result"]["body"]["memory"]) + " " + response["result"]["body"]["mem_type"])


#print(response)
