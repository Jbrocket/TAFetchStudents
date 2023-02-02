import os
from directoryManip import CreateDir, RemoveDir

def GetStudentDirs(cli_args: list(str), metadata):
    if len(cli_args) == 2:
        if not metadata['currentNDIds']:
            print("Error: Edit current saved data")
            os.exit(1)
        
    for NDid in metadata['currentNDIds']:
        CreateDir(NDid, metadata['assignmentNum'])