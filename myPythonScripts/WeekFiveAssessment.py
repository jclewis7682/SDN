##Author: Jesse Lewis##
##Date: 22FEB21##

##Week Five Assessment##


import requests
import json

"""
Be sure to run feature nxapi first on Nexus Switch

"""
switchuser='cisco'
switchpassword='cisco'

url='https://10.10.20.177/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ip interface brief",
      "version": 1
    },
    "id": 1
  }
]

'''

verify=False below is to accept untrusted certificate

'''

def vlan(answer):

    for name in answer["result"]["body"]["TABLE_intf"]["ROW_intf"]:

        print(name["intf-name"]+ "\t" + name["proto-state"] + "\t" +name["link-state"] + "\t" +name["prefix"])

response = requests.post(url,data=json.dumps(payload), verify=False,headers=myheaders,auth=(switchuser,switchpassword)).json()

print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")
print("-" * 4 + "\t" + "-" * 5 + "\t" + "-" * 4 + "\t" + "-" * 6 + "\t")
vlan(response)

#print(response)
