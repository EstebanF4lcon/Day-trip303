

from random import random
from re import X
from tkinter.messagebox import QUESTION

intro = "Welcome to Daytrip Gen 303"
print (intro)

ja="where is the daytrip headed too?"
print(ja)

options = "beach ,mountains , forest ,desert, random "
print (options) 


locations = input ("where are we headed today ?")

if locations == "beach":
    print("Clearwater,Florida !")

elif locations == "mountains":
    print("Estes Park, Colorado is my go to! ")
elif locations == "forest":
  print("Let's go to Tongass National Forest!")
elif locations =="desert":
 print ("Bring lots of water because Sahara Desert is hot !")
elif locations == "random":
  import random
  names = ["beach", "mountaions", "desert"]
  random_index = int(random.random() * len(names))
  random_name = names[random_index]
  print(random_name)
else :
  print("A random Trip awaits.")


be ="what type of restaurant do you prefer?"
print(be)

optionss="american cruisine,chinese food, mexican food ,fast food,random"
print(optionss)


food = input ("where are we eating today ?")

if food == "american cruisine":
    print("Outback Steakhouse. The Bloomin' Onion is famous for a reason! ")

elif food == "chinese food":
    print("Panda Express is one of my favorites!")

elif food == "mexican food":
    print("You can never go wrong with street tacos.")

elif food =="fast food":
    print ("Mcdonals Quick and Easy !")
elif food == "random":
  import random
  names = [" american cruisine" , "chinese food" , "mexican food" ,"fast food "]
  random_index = int(random.random() * len(names))
  random_name = names[random_index]
  print(random_name)
else :
   print("a random restrabant awaits")

print("We have to ride in style!")
ways_of_transportation= "Supercar,Lifted Truck,motorcycle, ecofrendly car, luxury car, random"
print(ways_of_transportation)

transportation = input ("how are we getting to our location? need transportation .")

if transportation == "supercar":
    print("Brand new 2020 buggati is ready!")

elif transportation == "lifted truck":
    print("2020 Ram trx one of the best trucks!")
elif transportation == "luxury car":
    print("Rolls Royce. This car is just like a dream coming true !")
elif transportation == "motorcycle":
  print("Make sure you wear a helment with your 2022 harley CVO roadglide.")
elif transportation =="ecofrendly car":
 print ("Spend less time at the pump and more inside the 2022 Honda Civic!")
elif transportation == "random":
  import random
  names = ["Supercar","lifted truck","motorcycle", "ecofrendly car","luxury car"]
  random_index = int(random.random() * len(names))
  random_name = names[random_index]
  print(random_name)
else :
  print("a random way of transportation awaits")

print("what are Adventure are we doing today?")
ways_of_entertainment= "swimming ,nature, sand dunes,hunting,random"
print(ways_of_entertainment)
entertainment = input ("What are we doing today?")

if entertainment == "swimming":
  print("Nothing like going to the beach for a swim!")

elif entertainment == "nature":
  print("Colorado has the best hikes around the Country!")

elif entertainment == "sand dunes":
  print("Off Road Advanture in Sand dunes of Arizona!")
    
elif entertainment == "hunting":
  print("Make sure you wear bring hunting wear!")

elif entertainment == "random":
  import random
  names = ["swimming ","nature", "sand dunes","hunting"]
  random_index = int(random.random() * len(names))
  random_name = names[random_index]
  print(random_name)
else :
  print("a random way of Adventure awaits")

print( "the location we are going is:" + locations)


print("lunch will be :"+ food)

print("Transportation in style is:"+ transportation)

print ("Stressfree advanture by:"+entertainment)

print("Complete thank you for using Daytrip Gen 303")