import json
import os

def loadJson(JSON: str):
    return json.load(open(JSON, 'r'))

def writeJson(data):
    try:
        os.remove("data/metadata.json")
    except FileNotFoundError:
        pass
    with open("metadata.json", 'xw') as f:
        json.dump(data, f, indent=4)
    return 0