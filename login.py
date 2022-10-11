import json
import os
import random
import time
from art import *

path = "players"
if not os.path.exists(path):
    os.makedirs(path)

def login():
    print("Welcome to the game!")
    tprint("Escape Room",font="rnd-small")
    choice = input("Do you have an account? y/n ")
    if choice.lower() == "n":
        signup()
    elif choice.lower() == "y":
        print("Login to the game".center(50,"-"),"\n")
        user = input("What is your username? ")
        password = input("What is your password? ")
        try:
            with open(os.path.join(path, user + ".json"), "r") as game:
                info = json.load(game)
            if info["username"] == user and info["password"] == password:
                print("Welcome to the game",user.title() + "!")
                #the game continues in main.py

                with open("current_player.json", "w") as file:
                    json.dump(info, file)
            else:
                print("Incorrect username or password, try again")
                login()
        except FileNotFoundError:
            print("\nWe can not find that account\nPlease try again\n")
            login()
    else:
        print("Please choose a valid option")
        login()

def signup():
    print("Account Signup".center(40,"-"))
    username = input("Please enter a username ")
    while True:
        password = input("Please enter a password ")
        confirm = input("Please confirm your password ")
        if password == confirm:
            break
        else:
            print("Invalid, your password does not match, please try again")

    powers = ["catches fish with your mind","cut coconut in half with a spoon","makes birysani appear out of thin air","able to lift a bus","able to fly at night","can turn tea into coffee","ability to talk to goats","pizza vision, can see a pizza anywhere in the world"]
    
    data = {}
    data["username"] = username
    data["password"] = password
    data["health"] = 100
    data["money"] = 0
    data["items"] = []
    data["start"] = time.time()
    data["powers"] = random.choice(powers)
    data["location"] = 0

    #check if the file is already in the folder, otherwise make it

    with open(os.path.join(path, username + ".json"), "w") as infile:
        data = json.dump(data, infile)

    login()
    

login()