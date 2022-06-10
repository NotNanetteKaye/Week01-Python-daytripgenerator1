import random
from unittest import result

destinations_list = ["Manila, Philippines", "Bogota, Columbia", "Barcelona, Spain", "Cancun, Mexico", "Los Angeles, California", "Australia"]
restaurants_list = ["Italian food", "Seafood", "Steakhouse", "Mediterreanean", "Vegeterian"]
mode_of_transportations = ["car", "plane", "train", "walk", "cruise"]
entertainments = ["beach", "hike", "bike", "club", "concerts", "art museums", "shopping"]


def random_item_picker(list):
    random_item = random.choice(list)
    return random_item


def destination_choice_confirmation():
    random_destination = random_item_picker(destinations_list)
    user_input = input(f"Welcome to Day Trip Generator! To begin let's choose a place. How does {random_destination} sound? Enter y/n: ")
    if user_input == "y":
        print("Yay, you have chosen a destination! Next let's think food. How does ")
        return random_destination
    elif user_input == "n":
        return destination_choice_confirmation()

confirmed_destination = destination_choice_confirmation()
# print(confirmed_destination)





# restaurant_choice = random_item_picker(restaurants_list)
# print(restaurant_choice)




# input(f"Welcome to Day Trip Generator to plan your ideal vacation! To begin, let's choose a location. How does {destination} sound? Enter y/n: ")