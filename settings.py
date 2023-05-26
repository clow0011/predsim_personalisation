import json

def getSettings():
    with open('settings.json') as json_file:
        settings = json.load(json_file)      
    
    return settings
