import json
import urllib.request
import random

def museum_painting():
  url = "https://collectionapi.metmuseum.org/public/collection/v1/departments" #the web adress with the information needed
  request = urllib.request.urlopen(url) #variable request to open the URL Library
  result = json.loads(request.read())
  
  return result["departments"][random.randint(1, 21)]["displayName"]