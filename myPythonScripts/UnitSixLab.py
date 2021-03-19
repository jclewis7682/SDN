##Author: Jesse Lewis##
##Date: 28FEB21##

##Unit Six Lab##


####Imports that need to be on to use APIs
import requests
import json

"""
Be sure to run feature nxapi first on Nexus Switch

"""
'''
####Part 1


###Creates a distionary of switches found in the Cisco dev environment
switches = {
    "dist-sw01" : {
        "hostname" : "dist-sw01",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.177",
        },

    "dist-sw02" : {
        "hostname" : "dist-sw02",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.178",
        },
    }


###fucntion to loop through the switches dictionary and print out the properties of each dictionary
def space(answer):

    for name in answer.keys():

        print(answer[name]["hostname"] + "\t" + answer[name]["deviceType"] + "\t\t" +answer[name]["mgmtIP"])

print("Host" + "\t\t" + "Type" + "\t\t" + "Mgmt IP")
print("-" * 46)
space(switches)

###Easy way to print the devices

print(switches["dist-sw01"]["hostname"] + "\t" + switches["dist-sw01"]["deviceType"] + "\t\t" + switches["dist-sw01"]["mgmtIP"] )
print(switches["dist-sw02"]["hostname"] + "\t" + switches["dist-sw02"]["deviceType"] + "\t\t" + switches["dist-sw02"]["mgmtIP"] )

###Part 2

###API call paramaters that are passed back to the website.
switchuser='cisco'
switchpassword='cisco'

###creates two variables with 2 different from the mgmt ips from the switches
url1='https://10.10.20.177/ins'
url2='https://10.10.20.178/ins'
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
#verify=False below is to accept untrusted certificate
'''

###What arguments are received back into variable response
###This pulls back the show version in response variable
###uses the 2 different urls
switch1 = requests.post(url1,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()
switch2 = requests.post(url2,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()


###function for pulling in both switch variables and printing out each switch detail
def vlan(answer):

    #for name in answer["result"]["body"]:
    switch = answer["result"]["body"]

    print(switch["host_name"] + "\t\t" + str(switch["memory"]) + "\t\t" + switch["mem_type"] + "\t\t" +switch["chassis_id"] + "\t\t" + switch["kick_file_name"])
        
print("Host" + "\t\t" + "Memory" + "\t\t" + "Memory Type" + "\t" + "Chassis" + "\t\t" + "Boot File")
print("-" * 120)
vlan(switch1)
vlan(switch2)
'''



###Part 3

###builds the switch dictionary
switches = {
    "dist-sw01" : {
        "hostname" : "dist-sw01",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.177",
        },

    "dist-sw02" : {
        "hostname" : "dist-sw02",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.178",
        },
    }


###creates a function to call each switch in the dictionary

def space(answer):

    ###starts the for loop of each switch in the dictionary
    for name in answer.keys():

        ###prints out the first switch details
        ###must be outside of the loop for it to print each switch individually
        print("\t")
        print(answer[name]["hostname"] + " OSPF Neighbors")
        print("Router-ID" + "\t\t" + "Neighbor ID" + "\t\t" + "Int")
        print("-" * 55)
        
        ###takes the mgmtIP from the each switch and sends it as an ip addr to the url
        url = 'https://'+str(answer[name]["mgmtIP"])+'/ins'

        switchuser='cisco'
        switchpassword='cisco'

        myheaders={'content-type':'application/json-rpc'}
        payload=[
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": "show ip ospf neighbor",
              "version": 1
            },
            "id": 1
          }
        ]

        response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()


        ###creates a variable of the switch fields
        rtr = response["result"]["body"]["TABLE_ctx"]["ROW_ctx"]["TABLE_nbr"]["ROW_nbr"]

        ###loops through each field and prints them
        for name in rtr:

                print(name["rid"] + "\t\t" + name["addr"] + "\t\t" + name["intf"])

        
###calls the space function with the input from switches dictionary
space(switches)



