#****************************************************************
#Name: Miguel Bezada
#Student Number: A00251474
#ANA1001 Final Project
#****************************************************************

import json 
import urllib.request
import login
from clear_screen import clear
import time
from bat import bat
from fairy import fairy
from weather import weather
from museum import museum_painting
import random
import os

time.sleep(2)
clear()

path = "players"

with open("current_player.json", "r") as game:
    info = json.load(game)

url = "https://raw.githubusercontent.com/miguelbezada/assignment8/main/escaperoom.json"
request = urllib.request.urlopen(url)
response = json.loads(request.read())

choice = input("Do you want to [start] over or [continue]? ")
if choice.lower() == "start":
    room = 0
    info.update({"health":100})
    #Update health to the temp file (current_player)
    info.update({"location":room})
    
    with open("current_player.json", "w") as file:
        json.dump(info, file)
      
    #Update health to the main file
    with open(os.path.join(path, info["username"] + ".json"), "w") as infile:
        json.dump(info, infile)
else:
    room = info["location"]

while True:
    time.sleep(1)
    clear()
    #print(info) #the players infomation
    print(f"""
        {info["username"].title()}, you are in {response[room]["name"].title()}
        You have {info["health"]}% health, ${info["money"]} and 
        Your power is {info["powers"]}
         """)

    health = info["health"]
  
    if response[room]["bat"] == 1:
        time.sleep(2)
        bat()
        attack = random.randint(1,10)
        print("You've been attacked by a bat")
        print("You loose", attack, "life points")
        health = health - attack
        info.update({"health":health})
        time.sleep(4)
        clear()
      
    if response[room]["fairy"] == 1:
        time.sleep(2)
        fairy()
        cure = random.randint(1,10)
        print("You've been healed by a fairy")
        print("You gain", cure, "life points")
        health = health + cure
        info.update({"health":health})
        time.sleep(4)
        clear()

    if response[room]["weather"] == 1:
        time.sleep(2)
        weather()
        time.sleep(5)
        clear()
    
    if response[room]["stranger"] == 1:
        print("**You see a stranger**")
        print("-----------------------")
        #connect to the stranger module 
        print("Stranger scares you!")
        time.sleep(5)
        clear()

    if response[room]["museum"] == 1:
        print(f"**You see a {museum_painting()} paiting**")
        print("-----------------------")
        #connect to the stranger module 
        time.sleep(5)
        clear()

    
    #print(response[room])
    print("-You are in",response[room]["name"].title(),"-")
    print("****************************************","\n")
    print(response[room]["story"])

    if response[room]["win"] == 1:
        print("~~~~You win!~~~~")
        time.sleep(5)
        print("Thank you for playing!")
        break
    elif response[room]["die"] == 1:
        print("~~~~You lose!~~~~")
        time.sleep(5)
        print("Thank you for playing!")
        break

    print("\n")
    print(response[room]["nav"].title())

    choice = input("Please make a choice: ")
    try:
        if choice == "1":
            room = response[room]["c1"] - 1
        elif choice == "2":
            room = response[room]["c2"] - 1
        elif choice == "3":
            room = response[room]["c3"] - 1
        else:
            print("Please pick a valid option")
    except:
        pass

    #save the progress to the temp file (current_player)
    info.update({"location":room})
    
    with open("current_player.json", "w") as file:
        json.dump(info, file)
      
    #update the player file in the player folder
    with open(os.path.join(path, info["username"] + ".json"), "w") as infile:
        json.dump(info, infile)
