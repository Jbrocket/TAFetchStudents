import os
from directoryManip import CreateDir, RemoveDir

def GetStudentDirs(cli_args: list(str), metadata):
    if not metadata['currentNDIds']:
        return
    if not metadata["assignmentNum"]:
        return
    if not metadata['']:
        return
    
    for NDid in metadata['currentNDIds']:
        CreateDir(NDid, metadata['assignmentNum'])