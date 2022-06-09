import random
import string
destinations = ["Manila, Philippines", "Bogota, Columbia", "Barcelona, Spain", "Cancun, Mexico", "Los Angeles, California", "Australia"]
restaurants = ["Italian food", "Seafood", "Steakhouse", "Mediterreanean", "Vegeterian"]
mode_of_transportation = ["car", "plane", "train", "walk", "cruise"]
entertainment = ["beach", "hike", "bike", "club", "concerts", "art museums", "shopping"]

random_destination = random.choice(destinations)
# print(random_destination)
destination_input = string(input(f"Welcome to Day Trip Generator! If you are not sure what you want to do for your vacation, you have come to the right place! We chose {random_destination} for your destination! Does that sound good? Enter y/n:"))
# print(destination_input)

for characters in destination_input:
    if characters == "y":
        print("yay!")
    else:
        print(string(input(f"Hmm let's try something else! How about {random_destination}?")))