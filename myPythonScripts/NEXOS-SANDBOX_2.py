##Author: Jesse Lewis##
##Date: 3MAR21##

##NEXOS-SANDBOX_2##


####Imports that need to be on to use APIs
import requests
import json

"""
Be sure to run feature nxapi first on Nexus Switch

"""
'''
####Part 1


###function to check hostname input
def hostName(answer):


    ###variable for special characters
    ###i left _ and - out because that is sometimes useful
    special_characters = "!@#$%^&*()+?=,<>/"

    ###checks to make sure the first character is not a digit
    if answer[0].isalpha():
        
        ###for loop to check for spaces
        for space in answer:

            if space.isspace() == True:

                print("Answer contain no spaces, begins with an alpha character and does not contain special characters")
                return False

        ###for loop to check for special characters
        for special in answer:

            if special in special_characters:
                print("Answer contain no spaces, begins with an alpha character and does not contain special characters")
                return False

                
        return True
        
    ###Blank input or any other input
    else:
        print("Answer contain no spaces, begins with an alpha character and does not contain special characters")

        result = False

    return result
    
###function to take the host name and send it to the switch
def changeHostName(answer):
    
    ###API call paramaters that are passed back to the website.
    switchuser='cisco'
    switchpassword='cisco'

    ###creates two variables with 2 different from the mgmt ips from the switches
    url='https://10.10.20.177/ins'
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
            ### answer is the validated hostname input
          "cmd": "hostname " + answer,
          "version": 1
        },
        "id": 2
      }
    ]


    
    #verify=False below is to accept untrusted certificate
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json()

######################################Start of the program
test1 = False
while test1 == False:

    ###User input to for hostname
    host = input("Please enter a new hostname: ")

    #calls hostName function
    check = hostName(host)

    if check == True:

        test1 = True

#calls the changeHostName function
changeHostName(host)
print("Hostname accepted.  Please check the device to confirm the hostname was chaged.")

###Validate by checking the siwtch

'''
#################Part 2


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


###function to modify the 3rd octet in and IP address
def modifyThirdOctet(ipAddr):

        #splits the input
        newAddr = ipAddr.split(".")

        ###adds 2 to the third octet
        sum = int(newAddr[2]) + 2

        ###deletes the original third octet value
        del newAddr[2]

        ###adds the new value into the third octet
        newAddr.insert(2, str(sum))

        
        modifiedIP = ""

        ###loop to put the ipAddr back in to the normal format
        for octetVal in newAddr:

            modifiedIP = modifiedIP + octetVal + "."

        modifiedIP = modifiedIP.rstrip(".")

        return modifiedIP


#creates a while loop to validate input from the input field
test2 = False
while test2 == False:  
    ipInput = input("Enter an IP address: ")

    ###checks to make sure the IP is valid
    validIP = checkIp(ipInput)
    
    #this result had to be set to True in order to work

    if validIP == True :

        ###if the ip is valid, this function does the math
        allTogether = modifyThirdOctet(ipInput)

        ###with the new ip address, we recheck to make sure it is still a valid ip address
        newAnswer = checkIp(allTogether)


        if newAnswer == True :

            
            print(allTogether)
            test2 = True
            


print("Your IP was accepted.  Thank you.")


            


