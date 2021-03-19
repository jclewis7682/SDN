##Author: Jesse Lewis##
##Date: 14FEB21##

##Unit Four Lab Homework##

import requests

'''
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload={}
headers = {
  'Cookie': '__cfduid=d2e4543878fdf381644761723d513ed0a1612898338'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

deck = response.json()


print("Your deck is shuffled and ready.  Your deck id = " + deck["deck_id"] + ".")

#or

deck_id = deck['deck_id']

print ("Your deck is shuffled and ready.  Your deck id = " + deck_id + ".")

print(response)

print(response["deck_id"])

#deck = response.json()
#deck_id = deck['deck_id']
#print(deck_id)


#Part 5

drawRequest = input("How many cards would you like to draw?: ")

url1 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + drawRequest

payload={}
headers = {
  'Cookie': '__cfduid=d2e4543878fdf381644761723d513ed0a1612898338'
}

response1 = requests.request("GET", url1, headers=headers, data=payload)

print(response1.text)
'''

######Part 8

######Function to ask the user if they want to play
def play(answer):

    ###Play on if the answer is yes
    if answer == "y" or answer == "Y":

        result = True

    ###Exits the game if no
    elif answer == "n" or answer == "N":
        print("Afraid? Want to rethink that answer?")
        
        result = exit()

    ###Blank input or any other input
    else:
        print("Answer must be a y or n")

        result = False

    return result


######Function to ask the user how many cards they want
def cards(answer):

    ###Starts a while function to test digits
    test0 = False
    while test0 == False :

        ###If a digit start
        if answer.isdigit() == True:


            ###Matches on 1 to 5
            if int(answer) >=1 or int(answer) <=5:
                test0 = True
                result = True

            ###If outside of 1 to 5
            if int(answer) <1  or int(answer) > 5:

                print("Cannot be anything but 1 thru 5")
                test0 = False
                result = False
                break          

        ###Blank input or any other input
        else:
            print("Please enter a number 1 thru 5")
            
            result = False
            break

    ###Returns the results        
    return result


###function to convert a,k,q,j to 10
def draw(answer):

    
    ###Returns the digit
    if answer.isdigit() == True:
        
        return answer

    ###Matches on a letter that returns 10 as the answer
    if answer.isdigit() != True:

        x = 10

        return x

###API call to the website
###This is after the first call to the website
def api(answer):

    ###Takes the deck_ID and firstDraw varaible to keep the same deck and input how many cards to draw
    url1 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + firstDraw

    payload={}
    headers = {}

    response2 = requests.request("GET", url1, headers=headers, data=payload)

    cardsDrawn = response2.json()

    ###returns the dictionary results based on how many cards the user input
    return cardsDrawn


###Function to get the number and suit of the card
def suit(answer):

    
    ###for loop that takes the information from the api dictionary results and iterates through
    for card in answer["cards"]:

        
        #newValue = int(draw(card["value"]))

        ###Returns each number and suit
        print("I drew a " + card["value"] + " of " + card["suit"])


###Function to add up all of the card values
def calc(answer):

    sum = 0

    ###Loops through each card value
    for card in answer["cards"]:
        

        ###looks at card value then checks to see if its a a,k,q,j to asign it a value of ten or keep the original number
        ###then converts it into an integer
        newValue = int(draw(card["value"]))


        ###adds the amount up in each loop
        sum = sum + newValue

    return sum


###Compares the sums of the computer vs the player to see who won
def final(comp, user):

    ###Computer wins
    if comp > user:
        print("\t")
        print("Better luck next time!")

    ###User wins
    if comp < user:
        print("\t")
        print("You got lucky!")

    ###Tie
    if comp == user:
        print("\t")
        print("Too bad for both of us!")



######################################Start of the program
test1 = False
while test1 == False:

    ###User input to play
    newGame = input("Do you want to play war with me (y or n): ")

    #calls play function
    answer = play(newGame)

    if answer != False:

        test1 = False

        break

###Game Instructions
print("\t")
print("This means war, which is what we will be playing but with a twist.")
print("\t")
print("We will each take turns drawing the same amount of cards untill all of the deck is used.")
print("\t")
print("Whoever has the highest total at the end, wins!")
print("\t")
print("Aces, Kings, Queens and Jacks count as 10 points.")
print("\t")

    
###API to shuffle 1 deck
###Can creat a function/input to shuffle more than 1 deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

###Returns the results of the shuffled deck
deck = response.json()

###Returns deck ID needed to play in the same deck
deck_id = deck['deck_id']

print ("Your deck is shuffled and ready.  Your deck id = " + deck_id + ".")
print("\t")

###Asks user how many cards to play with
test2 = False
while test2 == False:
    firstDraw = input("How many cards would you like to play with (1 thru 5): ")

    ###Calls cards function
    drawAnswer = cards(firstDraw)


    if drawAnswer == True:

        test2 = True


###Calls api function
cardsDrawn = api(deck)

###Takes the cards variable and calls suit function
suit(cardsDrawn)

###Takes the cards variable and calls calc function and converts the total into a string
print("That is "+ str(calc(cardsDrawn)) +" points for me.")


###Tells the user its their turn
print("\t")
print("\t")
print("\t")
print("Now your " + firstDraw + " cards.")
print("\t")
print("\t")
print("\t")


###Calls api function
myTotal = api(deck)


###Takes the total variable and calls suit function
suit(myTotal)

###Takes the total variable and calls calc function and converts the total into a string
print("That is "+ str(calc(myTotal)) +" points for you.")


###Takes the totals from both the computer and user and calls the final function to compare and see who the winner is
final(calc(cardsDrawn), calc(myTotal))
