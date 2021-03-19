##Author: Jesse Lewis##
##Date: 3FEB21##

##Python Dictionaries Homework##


#Defining the dictionary
router1 = {
    "hostname": "r1",
    "brand": "Cisco",
    "mgmtIP": "10.0.0.1",
    "interfaces" : {
        "G0/0": "10.1.1.1",
        "G0/1": "10.1.2.1",
        }
    }


########Part 3

print("router1 keys")
print(router1.keys())
print("\n")
print("\n")



print("router1[interfaces] keys")
print(router1["interfaces"].keys())
print("\n")
print("\n")



print("router1 values")
print(router1.values())
print("\n")
print("\n")



print("router1[interaces].values")
print(router1["interfaces"].values())
print("\n")
print("\n")



print("router1 items")
print(router1.items())
print("\n")
print("\n")



print("router1[interfaces] items")
print(router1["interfaces"].items())
print("\n")
print("\n")



########Part 4

#####iterate through individual interfaces
print(router1["interfaces"]["G0/0"])
print("\n")
print("\n")


#####iterate through individual interfaces
for interfaces in router1["interfaces"] :
    print(interfaces)
print("\n")
print("\n")


#####iterate through both keys and values
for interfaces in router1["interfaces"] :
    print(interfaces + " " * 5 + router1["interfaces"][interfaces])

print("\n")
print("\n")

########Part 5

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
        },

    "child2" : {
        "name" : "Tobias",
        "year" : 2007
        },

    "child3" : {
        "name" : "Linus",
        "year" : 2011
        }
    }

print(myfamily["child2"]["name"])
print("\n")
print("\n")

#for family in myfamily.keys() :
#    print(family + " " * 5 + myfamily.keys()[family])


########Part 6

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

#iterate through device [r1, r2, etc]
for ping in devices.keys():

    #returns the device key which is r1, then iterates through the mgmtIP key to return the value which is the IP address
    x = devices[ping]["mgmtIP"]
    print("ping  " + x)

    
