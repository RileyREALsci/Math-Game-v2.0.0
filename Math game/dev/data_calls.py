import random
import json
import base64
import time
from tkinter import ttk

#initalizations.

NEW_SAVE_DATA = {
    "name": "",
    "date": 0,
    "time_created": 0,
    "time_played": 0,
    "time_last_played": 0,
    "level": 0,
    "score": {
        "a": {
        "weak": "na",
        "easy": "na",
        "medium": "na",
        "hard": "na",
        "expert": "na",
        "ridiculous": "na",
        "impossible": "na"
        },
        "s": {
        "weak": "na",
        "easy": "na",
        "medium": "na",
        "hard": "na",
        "expert": "na",
        "ridiculous": "na",
        "impossible": "na"
        },
        "m": {
        "weak": "na",
        "easy": "na",
        "medium": "na",
        "hard": "na",
        "expert": "na",
        "ridiculous": "na",
        "impossible": "na"
        },
        "d/2": {
        "weak": "na",
        "easy": "na",
        "medium": "na",
        "hard": "na",
        "expert": "na",
        "ridiculous": "na",
        "impossible": "na"
        },
        "d": {
        "weak": "na",
        "easy": "na",
        "medium": "na",
        "hard": "na",
        "expert": "na",
        "ridiculous": "na",
        "impossible": "na"
        }
    },
    "items": {
    }
}

BOTS = {
    "bots": {
        "0": {
            "name": 0,
            "profile_discription": "",
            "age": 0,
            "gender": "",
            "level": 0,
            "skill_level": {
                "addition": 0,
                "subtraction": 0,
                "multiplication": 0,
                "devission": 0
            },
        }
    }
}

class GameData():

    def CallUserData(saveFile,path):
        f = open(f"data/saves/{saveFile}", "r")
        data = f.read()
        data = str.encode(data)
        data = base64.standard_b64decode(data)
        data = bytes.decode(data)
        convertedSingleQuotes = ''
        for s in data:
            if s == "'":
                s = '"'
                convertedSingleQuotes += s
            else:
                convertedSingleQuotes += s
        data = convertedSingleQuotes
        data = json.loads(data)
        data = data[path]
        return data

    def WriteData(saveFile,path,name): # Not tested
        """Updates user data when given a file and path refrence."""
        NEW_SAVE_DATA[path] = name # A variable obtained from the user interface when creating a new save.
        NEW_SAVE_DATA["time_created"] = time.time() # Creating time created on save.
        data = str(NEW_SAVE_DATA) # converting it to a string.
        data = str.encode(data)
        data = base64.standard_b64encode(data)
        data = bytes.decode(data)
        f = open(f"data/saves/{saveFile}", "w")
        f.write(str(data))
        
    
def trueOrFalseSave():
    """Telling the save menu interface the state of the save file chosen.
    returns a list for initalization on the menu program programm for condition checking"""

    f = open("data/saves/roaming.mg", "r")
    file = f.readline()
    roaminglist = file.split(" ") # is converting a string containing commas with list format to actual list.
    
    
    return roaminglist

def trueOrFalseSaveUpdate(roamingList): # Updates the roaming data file for refereces to non-used or used files.
    """Updates the roaming data file for refereces to non-used or used files."""

    f = open("data/saves/roaming.mg", "w")
    
    s = ' '.join([str(item) for item in roamingList])
    
    file = f.write(s)

def FactoryReset():
    saves = ["save1.mg","save2.mg","save3.mg","save4.mg"]
    for item in saves:
        NEW_SAVE_DATA["name"] = "NO_SAVE" # A variable obtained from the user interface when creating a new save.
        data = str(NEW_SAVE_DATA) # converting it to a string.
        data = str.encode(data)
        data = base64.standard_b64encode(data)
        data = bytes.decode(data)        
        f = open(f"data/saves/{item}", "w")
        f.write(str(data))

def getDate():
    stamp = time.time()
    hour = 3600
    day = 86400
    month = 2592000
    year = 31536000

    currentYear = (stamp / year + 1970)
    currentMonth = (stamp % year) / month
    currentDay = (int(stamp)) % month / day

    print(currentYear)
    print(currentMonth)
    print(currentDay)

class Graphis():
    def ReadGraphicDataFile(file,path):
        f = open(f"data/images/{file}", "r")
        data = f.read()
        convertedSingleQuotes = ''
        for s in data:
            if s == "'":
                s = '"'
                convertedSingleQuotes += s
            else:
                convertedSingleQuotes += s
        data = convertedSingleQuotes
        data = json.loads(data)
        data = data[path]
        return data
    
    def RendomizeTexture(graphicData):
        count = graphicData["count"]
        refrence = graphicData["refrence"]
        value = str(random.randint(1,count))
        path = graphicData[refrence + value] # this is the key name for the path in the json file.
        return path
        

#FactoryReset()