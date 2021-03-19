import requests

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
'''
print(response)

print(response["deck_id"])

#deck = response.json()
#deck_id = deck['deck_id']
#print(deck_id)
'''

#Part 5

drawRequest = input("How many cards would you like to draw?: ")

url1 = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + drawRequest

payload={}
headers = {
  'Cookie': '__cfduid=d2e4543878fdf381644761723d513ed0a1612898338'
}

response1 = requests.request("GET", url1, headers=headers, data=payload)

print(response1.text)

cardsDrawn = response1.json()

