import time
from os import system, name
  
# define our clear function
def clear():  
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def fairy():
    frames = [
        "\\0//",
        "--0--",
        "//0\\"
    ]
    
    for value in range(10):
        for frame in frames:
            print(frame)
            time.sleep(0.2)
            clear()
            