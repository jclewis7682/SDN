##Author: Jesse Lewis##
##Date: 31JAN21##

##Unit Two Lab Homework##

import re

#Defining the dictionary
router1 = {
    "brand": "Cisco",
    "model": "1941",
    "mgmtIP": "10.0.0.1",
    "G0/0": "10.0.1.1 /24",
    "G0/1": "10.0.2.1 /24",
    "G0/2": "10.0.3.1 /24",
    "hostname": "r1",
}


#########Part 1
'''
router1["model"] = "2901"
router1["G0/2"] = "10.1.3.1/24"

#########Part 2 - 1 way

nullValue = ""

for a, b in router1.items() :
    newValue = nullValue + "Key = " + a + "\t Value = " + b

    print(newValue)


#########Part 2 - 2 way (also added an additional tab (\t)

nullValue = ""

for key in router1.keys() :
    newValue = nullValue + "Key = " + key + "\t \t Value = " + router1[key]

    print(newValue)

'''
#########Part 3

#### sets null keyValue

keyValue = ""

#### loops through keys in router1 and adds x2 tabs
for keys in router1.keys():
    keyValue = keyValue + keys + "\t \t"


#### prints the loop from line 51
print(keyValue)


#### prints x150 -
print("-" * 150)


#### sets null valueValue
valuesValue = ""

#### loops through values in router1 and adds x2 tabs
for keys in router1.values():
    valuesValue = valuesValue + keys + "\t \t"


#### removes any /24 at the end of a value and replaces it with a blank
    newValue = valuesValue.replace("/24" , "")

##########still working on fixing the spacing issue
#    if valuesValue == "10.0.1.1 /24":
#        newValue = valuesValue + keys + "\t"

print(newValue)

#########Part 4


#### sets the first flag for the while loop
validName = False

while validName == False :


#### asks if you want to change the mgmt IP address
    
    mgmt = input("Do you want to change the Management IP address (y or n): ")

    if mgmt == "y":

#### if y, sets a new flag for a new while loop
        
        newName = False

        while newName == False:


#### input the ip address
            
            ipAddr = input("Enter an IP address for the Management Interface: ")

#### removes the "." in the address (numbers now are in a list ex: ['10' '1' '255' '255']
            
            newAddr = ipAddr.split(".")

#### ensures the length is for a x.x.x.x
            
            if len(newAddr) == 4:

#### if there are enough digits, iterate through the list
                
                for octet in newAddr :

#### if a letter is entered instead of a digit, then it breaks out of the for loop, tells the user and returns to the input at line 104
                    if octet.isdigit() != True :

                        print("ip address must be x.x.x.x where x>= 0 and x<= 255")

#### needs to be set to false it goes back through the while loop.  if set to true, then it continues to run
                        newName = False
                    
                        break


#### if all digits, the int command turns all strings into integers and have to be between 0 and 255                    
                    if int(octet) >= 0 and int(octet) <= 255 :


#### the loop is now true so we do not have to run again
                        newName = True
                        validName = True

#### if int(octet) is less than 0 and great than 255, it returns the user to input a correct ip address at line 104
                    else :
                
                        print("ip address must be x.x.x.x where x>= 0 and x<= 255")

                        newName = False
                        
                        break

#### outside the for loop, we ensure newName is equal to true (line 134)
                    
                if newName == True :


#### we use variable newValue from line 72 and replace the value in the key of mgmtIP with the user input from line 104
                    testValue = newValue.replace(router1["mgmtIP"] , ipAddr)

#### prints the new information out
                    print("Address Update!")
                    print(keyValue)
                    print("-" * 150)
                    print(testValue)

#### this else statement is tied to line 112 and if there are more or less than 4 strings in the list
            else :
                    
                print("IP address must be x.x.x.x where x>= 0 and x<= 255")


#### user input to line 91        
    if mgmt == "n":

        print("Nothing Changed!")
'''

#########Part 4 Extra Credit - Regex

#### sets the first flag for the while loop
validName = False

while validName == False :


#### asks if you want to change the mgmt IP address
    
    mgmt = input("Do you want to change the Management IP address (y or n): ")

    if mgmt == "y":

#### if y, sets a new flag for a new while loop
        
        newName = False

        while newName == False:


#### input the ip address
            
            ipAddr = input("Enter an IP address for the Management Interface: ")

#### removes the "." in the address (numbers now are in a list ex: ['10' '1' '255' '255']
            
            #newAddr = ipAddr.split(".")

#### ensures the length is for a x.x.x.x
            
            #if len(newAddr) == 4:

#### if there are enough digits, iterate through the list
                
                #for octet in newAddr :

#### if a letter is entered instead of a digit, then it breaks out of the for loop, tells the user and returns to the input at line 104
                    #if octet.isdigit() != True :

                        #print("ip address must be x.x.x.x where x>= 0 and x<= 255")

#### needs to be set to false it goes back through the while loop.  if set to true, then it continues to run
                        #newName = False
                    
                        #break


#### if all digits, the int command turns all strings into integers and have to be between 0 and 255                    

            
            pattern = "(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
            regex = re.compile(pattern)
            print([item for item in ipAddr if regex.match(item)])
            #if octet == re.match("\d {1,3}\.\d {1,3}\.\d {1,3}\.\d {1,3})/ OR /^\d+\.\d+\.\d+\.\d+$/", newAddr) :
                    #if int(octet) >= 0 and int(octet) <= 255 :


#### the loop is now true so we do not have to run again
            newName = True
            validName = True

#### if int(octet) is less than 0 and great than 255, it returns the user to input a correct ip address at line 104
            #else :
        
                #print("ip address must be x.x.x.x where x>= 0 and x<= 255")

                #newName = False
                
                #break

#### outside the for loop, we ensure newName is equal to true (line 134)
                    
                #if newName == True :


#### we use variable newValue from line 72 and replace the value in the key of mgmtIP with the user input from line 104
            testValue = newValue.replace(router1["mgmtIP"] , ipAddr)

#### prints the new information out
            print("Address Update!")
            print(keyValue)
            print("-" * 150)
            print(testValue)

#### this else statement is tied to line 112 and if there are more or less than 4 strings in the list
        else :
                
            print("IP address must be x.x.x.x where x>= 0 and x<= 255")


#### user input to line 91        
    if mgmt == "n":

        print("Nothing Changed!")

'''


