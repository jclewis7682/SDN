##Author: Jesse Lewis##
##Date: 27JAN21##

##Python Review 1 Homework##

'''
#####################Part 1 - Version one (long version)
fullName = input("What is your first and last name: ")

newName = fullName.split()
firstName = newName[0]
lastName = newName[1]

print("Welcome to Python, " + firstName.capitalize() + " is a really interesting surname! Are you related to the famous Victoria " + lastName.capitalize() + "?")


#####################Part 2 - Version two (shorter version)
fullName = input("What is your first and last name: ")

newName = fullName.split()

#newName[0] is firstname

print("Welcome to Python, " + newName[0].capitalize() + " is a really interesting surname! Are you related to the famous Victoria " + newName[1].capitalize() + "?")


#####################Part 2 Version one (long version)


#set the flag
validName = False

while validName == False :
    fullName = input("What is your first and last name: ")
    
#set variables before the if/else statements by spliting the results of the input into a string
    newName = fullName.split()

#this checks to make sure there are two strings from newName
#if it is 2, then it takes those inputs into first/last Name variables
    if len(newName) == 2 :
    
        firstName = newName[0]
        lastName = newName[1]

#now the statement is true and exits down to line 53
        validName = True

#if lens does not equal 2, then the user needs to reenter the input until its a valid input
    else :

        print("Please enter a first and last name")

print("Welcome to Python, " + firstName.capitalize() + " is a really interesting surname! Are you related to the famous Victoria " + lastName.capitalize() + "?")


#####################Part 2 Version two (short version)


#set the flag
validName = False

while validName == False :
    fullName = input("What is your first and last name: ")
    
#set variables before the if/else statements by spliting the results of the input into a string
    newName = fullName.split()

#this checks to make sure there are two strings from newName
#if it is 2, then it takes those inputs into first/last Name variables
    if len(newName) == 2 :
    

#now the statement is true and exits down to line 81
        validName = True

#if lens does not equal 2, then the user needs to reenter the input until its a valid input
    else :

        print("Please enter a first and last name")

print("Welcome to Python, " + newName[0].capitalize() + " is a really interesting surname! Are you related to the famous Victoria " + newName[1].capitalize() + "?")

'''
#####################Part 3 - Extra Credit


#set the flag
validName = False

while validName == False :
    fullName = input("What is your first and last name: ")
    
#set variables before the if/else statements by spliting the results of the input into a string
    newName = fullName.split()

#this checks to make sure there are two strings from newName
#if it is 2, then it takes those inputs into first/last Name variables
    if len(newName) == 2 :
    
        firstName = newName[0]
        lastName = newName[1] 

#checks both first/last Name variables to make sure they are only in the alphabet and they both have to be true
        if firstName.isalpha() == True & lastName.isalpha() == True :

        
#now the statement is true and exits down to line 119
            validName = True

#if there are characters other than alphabet letters, then the user needs to reenter the input until its a valid input
        else :

            print("Please enter a first and last name")

#if lens does not equal 2, then the user needs to reenter the input until its a valid input
    else :

        print("Please enter a first and last name")

print("Welcome to Python, " + firstName.capitalize() + " is a really interesting surname! Are you related to the famous Victoria " + lastName.capitalize() + "?")


