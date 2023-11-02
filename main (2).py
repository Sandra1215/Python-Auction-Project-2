startprice = 0 
current_bid = 0
answer =0
bidding = startprice,  current_bid, answer
item_name=0

def login(user_name, user_password):

 login(user_name, user_password)
user_name=input("What is your username?\n")
user_password = input("Enter your password\n")
while  user_password == input("Confirm your password\n"):
    print("Welcome to the auction!,", user_name) 
    break
  
else:    
    print("That is the wrong password. Try again")
    input("Enter your password\n")                   
    print("Welcome to the auction!,", user_name) 

print("Would you like to list an item?\n, Press 1 for yes, Press 2 no.\n") 
answer =int(input())

if (answer == 2) :
    print("good Bye")
else:
    print("What are you listing?\n")
item_name = input()

print("How much would you like it list the item for?\n")
startprice=input()

print("Would you like to place a bid?\n Press 1 for yes, Press 2 no.\n")
answer= int(input ())
if (answer == 2) :
  print("Sorry to here that, Good Bye")
  
while (answer == 1 and int(current_bid < int(startprice)) ):
  print("YES\nHow much would you like to bid?\n")
  current_bid = int(input()) 
  
  if (int(startprice) <= current_bid):

     print("You bid ", current_bid)
     print("You won the item!\n")
     
     payment_method = input("Would you like to pay with Cash or creDit? (c/d):")

     
     if payment_method == 'c':
      print("Please pay with cash within 24 hours\n")
     elif payment_method == 'd':
      print("Please pay with credit within 24 hours\n")
     else:
      print("Invalid payment method. Please try again.\n")
      continue
     
     print("Auction is closed") 

  elif (int(startprice) >= current_bid):
      print("Sorry, your bid was below minium price\n")
      print("Would you like to make another bid?\n")
       # can place another bid 
        #if bid was too low
      print(" Press 1 for yes, Press 2 no.\n")
      answer=int(input())
if (answer == 2) :
      print("good Bye")








