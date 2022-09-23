import random
from unittest import result

destinations_list = ["Manila, Philippines", "Bogota, Columbia", "Barcelona, Spain", "Cancun, Mexico", "Los Angeles, California", "Australia"]
restaurants_list = ["Italian food", "Seafood", "Steakhouse food", "Filipino food", "Mediterreanean food", "Vegeterian food"]
mode_of_transportations_list = ["car", "plane", "train", "walking", "cruise"]
entertainments_list = ["go to the beach", "go hike", "go biking", "go to clubs", "go to concerts", "go to art museums", "go shopping"]


def random_item_picker(list):
    random_item = random.choice(list)
    return random_item


def destination_choice_confirmation():
    random_destination = random_item_picker(destinations_list)
    user_input = input(f"Welcome to Day Trip Generator! To begin let's choose a place. How does {random_destination} sound? Enter y/n: ")
    if user_input == "y":
        print("Yay, you have chosen a destination! Next let's think food.")
        return random_destination
    elif user_input == "n":
        return destination_choice_confirmation()

confirmed_destination = destination_choice_confirmation()

def restaurant_choice_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_restaurant = random_item_picker(restaurants_list)
        user_input = input(f"How does {random_restaurant} sound? Enter y/n: ")
        if user_input == "y":
            print("Yay, you have chosen a restaurant! Next let's think about how you will get there.")
            return random_restaurant
        else:
            print("Let's brainstorm something else!")

confirmed_restaurant = restaurant_choice_confirmation()
        

def transportation_choice_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_transportation = random_item_picker(mode_of_transportations_list)
        user_input = input(f"How does {random_transportation} sound? Enter y/n: ")
        if user_input == "y":
            print("Yay, you have chosen your mode transportation! Next let's think about the fun things you will do when you arrive!")
            return random_transportation
        else:
            print("There are multiple types of transportation!")

confirmed_transportation = transportation_choice_confirmation()

def entertainment_choice_confirmation():
    user_confirmed = False
    while user_confirmed == False:
        random_entertainment = random_item_picker(entertainments_list)
        user_input = input(f"How does {random_entertainment} sound? Enter y/n: ")
        if user_input == "y":
            print("Yay, you have chosen your fun events!")
            return random_entertainment
        else:
            print("Let's think of something else!")

confirmed_entertainment = entertainment_choice_confirmation()

confirming_details = input(f"Sweet we have generated your day trip! Now let's confirm the details. The trip generated is destination: {confirmed_destination}, restaurant: {confirmed_restaurant}, transportation: {confirmed_transportation}, and entertainment: {confirmed_entertainment}. Does everything look correct? Enter y/n:")
if confirming_details == "y":
    print(f"Yay! So it looks like you will be going to {confirmed_destination}! You will eat {confirmed_restaurant}. You will travel by {confirmed_transportation}. For fun, you will {confirmed_entertainment}. Sounds like the dream vacation to me!")
else:
    print("Uh oh! Looks like we will have to start over.")
