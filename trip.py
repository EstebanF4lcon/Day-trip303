print("hello welcome to Daytrip Gen 303 2.0!")


import random

restaurant_list =["Texas Roadhouse", "Red Robins ","Pf Chang","Tacos el Gordo","Cici's pizza"]
location_list= ["Beach" ,"Mountains" , "Forest" ,"Desert ", "Island","Internatinal"]
entertainment_list = ["Clubing", "Swiming","Off road","Hunting","Shoping"]
transportation_list = ["Supercar","Ecofrendly car","Limo","Uber","Bus"]

def choose_random_value(list):
  chosen_value = random.choice(list)
  return chosen_value

restaurant = choose_random_value(restaurant_list)
location = choose_random_value(location_list)
entertainment = choose_random_value(entertainment_list)
transportation = choose_random_value(transportation_list)


def choose_restaurant():
  restaurant = choose_random_value(restaurant_list)
  user_is_happy = False
  while user_is_happy == False:
    user_input =input(f"We are eating {restaurant} ! Is this Restaurant okay with you? Please answer 'y or n'")
    if user_input == "y":
      print(f"Great selection enjoy your food! {restaurant}!")
      user_is_happy=True
    elif user_input == 'n':
      restaurant = choose_random_value(restaurant_list)
    

chosen_restaurant = choose_restaurant()

def choose_location():
  location = choose_random_value(location_list)
  user_is_happy = False
  while user_is_happy == False:
    user_input = input(f"The next trip is at {location} ! Are you sure you want to go there ? Please answer 'y or n'")
    if user_input == "y":
      print(f"Enjoy your trip, to the {location}!")
      user_is_happy=True
    elif user_input== "n":
      location= choose_random_value(location_list)

chosen_location = choose_location()


def choose_entertainment():
  entertainment = choose_random_value(entertainment_list)
  user_is_happy = False
  while user_is_happy == False:
    user_input =input(f"Our next advanture will be {entertainment} ! is that fine with you? Please answer 'y or n'")
    if user_input == "y":
      print(f"Have fun, {entertainment}!")
      user_is_happy=True
    elif user_input== "n":
      entertainment= choose_random_value(entertainment_list)

chosen_entertainment = choose_entertainment()


def choose_transportation():
  transportation = choose_random_value(transportation_list)
  user_is_happy = False
  while user_is_happy == False:
    user_input =input(f"Our way to get there is {transportation} ! You want take this? Please answer 'y or n'")
    if user_input == "y":
      print(f"Riiding in style with the {transportation} have a safe trip!")
      user_is_happy=True
    elif user_input== "n":
      transportation= choose_random_value(transportation_list)

chosen_transportaion=choose_transportation()  

print(f"First of all we need a way to get around in {chosen_transportaion}. Stopping by to get some food at {chosen_restaurant}. Then we'll go to the {chosen_location}. Last but not least we'll {chosen_entertainment}.")