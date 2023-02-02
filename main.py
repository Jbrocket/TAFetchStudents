#!/usr/bin/env python3

import sys
from utils.directoryManip import CreateDir, RemoveDir
from utils.dataManip import loadJson, writeJson
from utils.cli import GetStudentDirs, EditMetadata

if __name__ == "__main__":
    options = set(["import", "edit", "remove", "compile", "distribute"])
    
    try:
        if sys.argv[1] not in options:
            print("Usage: ./main.py <import|edit|remove|compile|distribute> <OPTIONS>\n\
The options will be highlighted in the README.md\nPlease call \
this module from the folder that you want the directories in.")
            sys.exit(1)
    except IndexError:
        print("Usage: ./main.py <import|edit|remove|compile|distribute> <OPTIONS>\n\
The options will be highlighted in the README.md\nPlease call \
this module from the folder that you want the directories in.")
        sys.exit(1)
    
    metadata = loadJson('metadata.json')
    
    if sys.argv[1] == "edit":
        EditMetadata()
    elif sys.argv[1] == "import":
        GetStudentDirs()
    
    try:
        fp = open(sys.argv[1], "r")
        for NDid in fp.readlines():
            CreateDir(NDid.strip(), sys.argv[2])
    except FileNotFoundError:
        for NDid in  map(lambda x: x.lower(), sys.argv[1].split(",")):
            CreateDir(NDid.strip(), sys.argv[2])
            
    writeJson(metadata)