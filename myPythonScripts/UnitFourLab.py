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
def first(answer):

    if answer == "y" or answer == "Y":

        result = True

    elif answer == "n" or answer == "N":
        print("Afraid? Want to rethink that answer?")
        
        result = False

    else:
        print("Answer must be a y or n")

        result = False

    return result

def second(answer):

    test0 = False
    while test0 == False :
        if answer.isdigit() == True:
                
            if int(answer) >=1 or int(answer) <=5:
                test0 = True
                result = True

            if int(answer) <1  or int(answer) > 5:

                print("Cannot be anything but 1 thru 5")
                test0 = False
                result = False
                break          

        else:
            print("Please enter a number 1 thru 5")
            
            result = False
            break
        
    return result

###function to convert a,k,q,j to 10

def third(answer):

    #number = answer()

    if answer.isdigit() == True:
        
        return answer

    if answer.isdigit() != True:

        x = 10

        return x

def final(comp, user):

    if comp > user:
        print("\t")
        print("Better luck next time")

    if comp < user:
        print("\t")
        print("You got lucky")

    if comp == user:
        print("\t")
        print("Too bad for both of us")
    
    
test1 = False
while test1 == False:
    newGame = input("Do you want to play war with me (y or n): ")

    answer = first(newGame)

    if answer != False:

        test1 = False

        break

print("\t")
print("This means war, which is what we will be playing but with a twist.")
print("\t")
print("We will each take turns drawing the same amount of cards untill all of the deck is used.")
print("\t")
print("Whoever has the highest total at the end, wins!")
print("\t")
print("Aces, Kings, Queens and Jacks count as 10 points.")
print("\t")

    

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

deck = response.json()

deck_id = deck['deck_id']

print ("Your deck is shuffled and ready.  Your deck id = " + deck_id + ".")
print("\t")


test2 = False
while test2 == False:
    firstDraw = input("How many cards would you like to draw (1 thru 5): ")

    drawAnswer = second(firstDraw)


    if drawAnswer == True:

        test2 = True


url1 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + firstDraw

payload={}
headers = {}

response2 = requests.request("GET", url1, headers=headers, data=payload)

cardsDrawn = response2.json()

sum = 0

for card in cardsDrawn["cards"]:

    cardValue = third(card["value"])
    newValue = int(cardValue)
    #print(newValue)
    #input("")

    sum = sum + newValue
    computerTotal = sum

    
    print("I drew a " + card["value"] + " of " + card["suit"])
print("That is "+ str(computerTotal) +" points for me.")
print("\t")
print("\t")
print("\t")
print("Now your " + firstDraw + " cards.")
print("\t")
print("\t")
print("\t")

####my draw

url2 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + firstDraw

payload={}
headers = {}

response3 = requests.request("GET", url2, headers=headers, data=payload)

cardsDrawn = response3.json()

myTotal = 0

for card in cardsDrawn["cards"]:

    cardValue = third(card["value"])
    newValue = int(cardValue)
    #print(newValue)
    #input("")

    myTotal = myTotal + newValue
   

    
    print("You drew a " + card["value"] + " of " + card["suit"])
print("That is "+ str(myTotal) +" points for you.")

final(computerTotal, myTotal)
