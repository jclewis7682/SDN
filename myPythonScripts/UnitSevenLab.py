##Author: Jesse Lewis##
##Date: 8MAR21##

##Unit Seven Lab##


import requests
import json


"""
Be sure to run feature nxapi first on Nexus Switch

"""

###function to check if the switch interface is already on the switch
def switchInterface(check):

    ###calls the vlanInts - is a list of interface names
    ###if it is equal to the users input then returns true
    if check in vlanInts:

        return True

    else:

        print("Please enter an interface shown from the list")

        return False



###function to check IP input
def checkIp(ipAddr) :

        
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


###function to check subnet mask input
def checkSubnet(mask) :

        
        #splits the input
        newMask = mask.split(".")

        #test the ip length
        if len(newMask) == 4:

            #sets the while loop flag
            

            #starts a loop to check and see if there is any letters in the ip
            for octet in newMask :
                if octet.isdigit() != True :

                    #if there are, then prints out below, keeps the loop true but function result false
                    print("Subnet mask must be x.x.x.x where x>= 0 and x<= 255")
                    test0= True
                    return False
                

                if octet.isdigit() == True:
                    
                    if int(octet) < 0 or int(octet) > 255:
                        
                        #if the conditions are not met, then prints out below, keeps the loop true but function result false
                        print("Subnet mask must be x.x.x.x where x>= 0 and x<= 255")
                        test0 = True
                        return False
                       

                        #send the final return results back
            return True

        #if the ip length isnt 4, then the function is false                    
        else:
            print("Subnet mask must be x.x.x.x where x>= 0 and x<= 255")
            test0 = False
            return False


###function to add the user input back onto the switch
def changeAddress(switchIP, switchInt, ipInput, subNet):
    
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
          "cmd": "interface " + switchInt,
          "version": 1
        },
        "id": 2
      },
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            ###Addes the new IP address and subnet mask
          "cmd": "ip address " + ipInput + " " + subNet,
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
    intList=[]
    print("Name" + "\t" + "Proto" + "\t" + "Link" + "\t" + "Address")
    print("-" * 4 + "\t" + "-" * 5 + "\t" + "-" * 4 + "\t" + "-" * 6 + "\t")
    
    ###loops through switch interfaces
    for name in response["result"]["body"]["TABLE_intf"]["ROW_intf"]:

        print(name["intf-name"]+ "\t" + name["proto-state"] + "\t" +name["link-state"] + "\t" +name["prefix"])

        ###adds/appends all of the interface names to the null list
        intList.append(name["intf-name"])

    ###returns all of the results of the new list interface names
    return intList


###checks for valid y/n input
def checkAnswer(answer):

    ###Play on if the answer is yes
    if answer == "y" or answer == "Y":

        result = True

    ###Exits the game if no
    elif answer == "n" or answer == "N":

        result = True

    ###Blank input or any other input
    else:
        print("Answer must be a y or n")

        result = False

    return result



###Start of the program
test1 = False
while test1 == False:

    ###user enters ip address of the switch they want to use
    ###in this example, we only have 10.10.20.177 and .178 working so those have to be entered
    switchIP = input("Please enter the switch management IP address: ")

    ###adds the ip address to the vlanShow function
    vlanInts = vlanShow(switchIP)

    test2 = False
    while test2 == False:

        ###Vlan/Eth interface input
        print("\t")
        switchInt = input("Which interface would you like to change the address on?: ")
        print("\t")

        check = switchInterface(switchInt)


        if check == True:

             test2 = False

             break

    ###IP interface input
    test3 = False
    while test3 == False:
        print("\t")
        ipInput = input("Enter an IP address for the Interface: ")
        print("\t")

        ipAnswer = checkIp(ipInput)


        if ipAnswer == True :

            test3 = False

            break


    ###Subnet input
    test4 = False
    while test4 == False:
        print("\t")
        print("Please enter the subnet mask like 255.255.128.0")
        print("\t")
        subNet = input("Enter a Subnet Mask: ")
        print("\t")

        subAnswer = checkSubnet(subNet)


        if subAnswer == True :

            test4 = False

            break

    ###One last check before sending the information/cmds to the switch
    test5 = False
    while test5 == False:

        print("\t")
        print(switchInt, ipInput, subNet)
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
changeAddress(switchIP, switchInt, ipInput, subNet)
print("\t")

###prints the new info
print(vlanShow(switchIP))
print("\t")
print("Your information has been updated.  If you do not see the IP updated, your subnet mask did not take. Please run again.")
