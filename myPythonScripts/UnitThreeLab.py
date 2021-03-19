##Author: Jesse Lewis##
##Date: 7FEB21##

##Unit Three Lab Homework##

'''
#####################Part 1
def name(fullName):
    #set variables before the if/else statements by spliting the results of the input into a string
    newName = fullName.split()


#this checks to make sure there are two strings from newName
#if it is 2, then it takes those inputs into first/last Name variables
    if len(newName) == 2 :


#now the statement is true and exits down to line 53
        result = True

        #if lens does not equal 2, then the user needs to reenter the input until its a valid input
    else :

        result = False

        
    return result

#set the flag
validName = False

while validName == False :
    testName = input("What is your first and last name: ")

    validName = name(testName)

    if validName == False:
        print("Please enter a first and last name")
    
fullName = testName.split()
firstName = fullName[0]
lastName = fullName[1]


print("Welcome to Python, " + firstName.capitalize() + ". " + lastName.capitalize() + " is a really interesting surname! Are you related to the famous Victoria " +lastName.capitalize() + "?")


#####################Part 2a

ntpServer = {
    "Server1": "221.100.250.75",
    "Server2": "201.0.113.22",
    "Server3": "58.23.191.6",
    }


print("Server name" + "\t" + "Address")
print("_"*25)
for ips in ntpServer.keys() :

    print(ips + "\t\t" + ntpServer[ips])

#print(ntpServer.keys() + "\t" + ntpServer["Server1"])


#####################Part 2b

def server(ips):

    print("Server name" + "\t" + "Address")
    print("_"*25)
    for newServer in ips.keys() :

        print(newServer + "\t\t" + ips[newServer])

ntpServer = {
    "Server1": "221.100.250.75",
    "Server2": "201.0.113.22",
    "Server3": "58.23.191.6",
    }


server(ntpServer)



#####################Part 3
def pingPrep(ipList) :

    for ping in ipList.values() :

        print("Ping " + ping)

    
ntpServer = {
    "Server1": "221.100.250.75",
    "Server2": "201.0.113.22",
    "Server3": "58.23.191.6",
    }


pingPrep(ntpServer)


'''
#####################Part 4


#ping function
def pingPrep(ipList) :

    for ping in ipList.keys():

    #returns the device key which is r1, then iterates through the mgmtIP key to return the value which is the IP address
        x = devices[ping]["mgmtIP"]
        print("ping  " + x)


#function for the first input
def first(answer):

    if answer == "y":

        return True

    elif answer == "n":
        print("Nothing Changed!")
        
        return False

    else:
        print("Answer must be a y or n")

        return False

    

# function for responses to device name, type, and brand
def second(answer):

    if answer == "":
        print("Please enter a valid name.")

        result = False

    else:

        result = True

    return result

#function to validate IP address input
def ip(ipAddr) :

        
        #splits the input
        newAddr = ipAddr.split(".")

        #test the ip length
        if len(newAddr) == 4:

            #sets the while loop flag
            test0 = False
            while test0 == False : 

                #starts a loop to check and see if there is any letters in the ip
                for octet in newAddr :
                    if octet.isdigit() != True :

                        #if there are, then prints out below, keeps the loop true but function result false
                        print("IP address must be x.x.x.x where x>= 0 and x<= 255")
                        test0= True
                        result = False
                        break
                    

                    if octet.isdigit() == True:
                        
                        if int(octet) < 0 or int(octet) > 255:
                            
                            #if the conditions are not met, then prints out below, keeps the loop true but function result false
                            print("IP address must be x.x.x.x where x>= 0 and x<= 255")
                            test0 = True
                            result = False
                            break

                        #if a valid ip, then exits the initial while loop and sets the results to true for the function
                        if int(octet) >=0 or int(octet) <= 255:
                            test0 = False
                            result = True

                #send the final return results back
                return result

        #if the ip length isnt 4, then the function is false                    
        else:
            print("IP address must be x.x.x.x where x>= 0 and x<= 255")
            test0 = False
            result = False

#base devices dictionary
devices = {
    "R1" : {
        "type" : "router",
        "hostname" : "R1",
        "mgmtIP" : "10.0.0.1"
        },
    
    "R2" : {
        "type" : "router",
        "hostname" : "R2",
        "mgmtIP" : "10.0.0.2"
        },
    
    "S1" : {
        "type" : "switch",
        "hostname" : "S1",
        "mgmtIP" : "10.0.0.3"
        },

    "S2" : {
        "type" : "switch",
        "hostname" : "S2",
        "mgmtIP" : "10.0.0.4"
        },
    }

#sets the while loop flag
validName = False

while validName == False :

    #creates a while loop to validate input from the input field
    test1 = False
    while test1 == False:
        newDevice = input("Do you want add a new device (y or n): ")

        answer = first(newDevice)

        if answer != False:

            test1 = False

            break

    #creates a while loop to validate input from the input field
    test2 = False
    while test2 == False:    
        deviceName = input("What is the name of the device: ")

        name = second(deviceName)

        if name != False:

            test2 = False

            break

    #creates a while loop to validate input from the input field
    test3 = False
    while test3 == False:  
        deviceType = input("What is the device type (router or switch): ")

        typeOf = second(deviceType)

        if typeOf != False:

            test3 = False

            break

    #creates a while loop to validate input from the input field
    test4 = False
    while test4 == False: 
        brandName = input("What is the brand name: ")

        brand = second(brandName)

        if brand != False:

            test4 = False

            break

    #creates a while loop to validate input from the input field
    test5 = False
    while test5 == False:  
        ipInput = input("Enter an IP address for the Management Interface: ")

        ipAnswer = ip(ipInput)

        #this result had to be set to True in order to work
        print(ipAnswer)
        x=input("")
        if ipAnswer != False :

            test5 = True

    
        #sets a new variable by taking the inputs from the variables above
        devices[deviceName] = {"hostname" : deviceName, "type" : deviceType, "brand" : brandName, "mgmtIP" : ipInput}


    #displays the new dictonary and pings the mgmtIP
    print("\n")
    print("New Dictionary Key is " + deviceName + " \n")
    print(devices[deviceName])
    print("\n")
    print(pingPrep(devices))
    print("All information has been input.  Thank you.")

        
