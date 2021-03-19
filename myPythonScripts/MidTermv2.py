##Author: Jesse Lewis##
##Date: 14MAR21##

##Midterm##


import requests
import json


"""
Be sure to run feature nxapi first on Nexus Switch

"""

###Dictionary of Switches
devices = {
    "dist-sw01" : "10.10.20.177",
    "dist-sw02" : "10.10.20.178",
    }


###function to check IP input
def checkIp(listIPs) :

    for ipAddr in listIPs :
    
        #splits the input
        newAddr = ipAddr.split(".")

        #test the ip length
        if len(newAddr) == 4:

            #sets the while loop flag
            

            #starts a loop to check and see if there is any letters in the ip
            for octet in newAddr :
                if octet.isdigit() != True :

                    #if there are, then prints out below, keeps the loop true but function result false
                    print("IP address must be x.x.x.x where x>= 0 and x<= 255")
                    test0= True
                    return False
                

                if octet.isdigit() == True:
                    
                    if int(octet) < 0 or int(octet) > 255:
                        
                        #if the conditions are not met, then prints out below, keeps the loop true but function result false
                        print("IP address must be x.x.x.x where x>= 0 and x<= 255")
                        test0 = True
                        return False
                       

                        #send the final return results back
            return True

        #if the ip length isnt 4, then the function is false                    
        else:
            print("IP address must be x.x.x.x where x>= 0 and x<= 255")
            test0 = False
            return False



###function to modify the 4th octet in and IP address
def modifyForthOctet(ipAddr):
    
    ipList=[]
    for ip in ipAddr:

        #splits the input
        newAddr = ip.split(".")

        ###adds 2 to the third octet
        sum = int(newAddr[3]) + 5

        ###deletes the original third octet value
        del newAddr[3]

        ###adds the new value into the third octet
        newAddr.insert(3, str(sum))

        
        modifiedIP = ""

        ###loop to put the ipAddr back in to the normal format
        for octetVal in newAddr:

            modifiedIP = modifiedIP + octetVal + "."

        modifiedIP = modifiedIP.rstrip(".")

        ###adds/appends all of the interface names to the null list
        ipList.append(modifiedIP)

    ###returns all of the results of the new list interface names

    return ipList


###function to add the vlan interface and ip address of the vlan back into a dictionary
def vlanDict(vlan, ip):

    ###sets a blank dictionary
    thisDict = {}


    ###To-Do: create a test to see if both lists are the same length

    ###loops through each vlan
    for vlanInt in vlan:

        ###loops through each ip addr
        for ipNum in ip:


            ###takes the first ip and pairs it with the first key
            thisDict[vlanInt] = ipNum
            
            ###these two parts are needed.  the remove, removes the first ip
            ###from the list so the for loop does not keep looping till the last ip
            ###the break stops it at that first ip
            ip.remove(ipNum)
            break

    ###returns the full dictionary
    return thisDict

###another way to add to the dictionary
'''
    for x in range(0, (len(vlan) - 1)):

        thisDict[vlan[x]] = ip[x]
        print(x)
'''




###checks for valid y/n input
def checkAnswer(answer):

    ###Play on if the answer is yes
    if answer == "y" or answer == "Y":

        result = True

    ###Exits the game if no
    elif answer == "n" or answer == "N":

        result = False
        exit()

    ###Blank input or any other input
    else:
        print("Answer must be a y or n")

        result = False

    return result


###function to add the user input back onto the switch
def changeAddress(switchIP, updatedDict):

    ###Loops through all
    for finalDict in updatedDict:

            ###API call paramaters that are passed back to the website.
            switchuser='cisco'
            switchpassword='cisco'

            ###passes the switchesIP to the url
            url='https://'+str(switchIP)+'/ins'
            myheaders={'content-type':'application/json-rpc'}
            payload=[
              {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                  "cmd": "configure terminal",
                  "version": 1
                },
                "id": 1
              },
              {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    ###Passes the interface name
                  "cmd": "interface " + finalDict,
                  "version": 1
                },
                "id": 2
              },
              {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    ###Addes the new IP address and subnet mask
                  "cmd": "ip address " + updatedDict[finalDict] + " 255.255.255.0",
                  "version": 1
                },
                "id": 3
              }
            ]


            response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()

        
####Shows the interfaces
def vlanShow(IP):
    switchuser='cisco'
    switchpassword='cisco'

    url='https://'+str(IP)+'/ins'
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

    #verify=False below is to accept untrusted certificate

    '''

    response = requests.post(url,data=json.dumps(payload), verify=False,headers=myheaders,auth=(switchuser,switchpassword)).json()

    ###creates a blank/null list
    ipList=[]
    vlanList=[]
    print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")
    print("-" * 4 + "\t" + "-" * 5 + "\t" + "-" * 4 + "\t" + "-" * 6 + "\t")
    
    ###loops through switch interfaces
    for name in response["result"]["body"]["TABLE_intf"]["ROW_intf"]:

        ###creates a variable to check for only vlans
        vlanCheck = name["intf-name"]

        ###if it starts with a V, it will pull the vlans
        if vlanCheck.startswith("V") :
            print(name["intf-name"]+ "\t" + name["proto-state"] + "\t" +name["link-state"] + "\t" +name["prefix"])

        ###adds/appends all of the interface names and ips to the null list

            vlanList.append(name["intf-name"])
            ipList.append(name["prefix"])
            

    ###returns all of the results of the new list interface names
            
    return vlanList, ipList






#############Start of the program
test0 = False
while test0 == False:


    test1 = False
    while test1 == False:
        print("We will be updating the following switches:")
        print("\t")
        print(devices.keys())
        print("\t")
        firstQ = input("Would you like to procedue? (y or n): ")


        answer = checkAnswer(firstQ)

        if answer == True:

            test1 = False

            break

    ###this starts the loop to iterate through the device ips and to send them to the switch url
    for switchIP in devices.values():

        print("\t")
        print("We will adjust the following IP: " +switchIP)
        print("\t")
    ###adds the ip address to the vlanShow function
        vlanInts, vlanIPs = vlanShow(switchIP)


        ###IP interface input
        test3 = False
        while test3 == False:
            print("\t")
            ipInput = input("Do you want to increase each Vlan IP address by 5 (y or n): ")
            print("\t")

            ipAnswer = checkAnswer(ipInput)


            if ipAnswer == True :

            ###if the ip is valid, this function does the math for the 4th octet
                allTogether = modifyForthOctet(vlanIPs)
                
            ###with the new ip address, we recheck to make sure it is still a valid ip address
                newAnswer = checkIp(allTogether)


                if newAnswer == True :
                    
                    test3 = False

                    break

        ###sends it to combine the vlan interface and ips into a dictionary
        updatedDict = vlanDict(vlanInts, allTogether)

        ###One last check before sending the information/cmds to the switch
        test5 = False
        while test5 == False:

            print("\t")
            print(updatedDict)
            print("\t")
            validateAnswer = input("Is this information correct (y or n): ")
            print("\t")

            goodA = checkAnswer(validateAnswer)

            ###checks user input
            if goodA == True :

                ###if a y or n returns back as true, this checks for a y to continue the program
                if validateAnswer.upper() == "Y" :
                
                    test1 = True
            
                    break

                ###or if anything else, then kicks them back to the start to redo the input
                else:
                    break

        ###sends all of the inputs to the changeAddress variable
        changeAddress(switchIP, updatedDict)
        print("\t")

        ###prints the new info
        vlanShow(switchIP)
        print("\t")
        print("Your information has been updated.")

    print("\t")
    print("Your switches have been updated.")
    break
    
