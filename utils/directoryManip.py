import os
import shutil

def CreateDir(NDid: str, ChallengeNum: str):
    try: 
        os.mkdir(f"{os.getcwd()}/{NDid}Challenge{ChallengeNum}")
    except FileExistsError:
        shutil.rmtree(f"{os.getcwd()}/{NDid}Challenge{ChallengeNum}", ignore_errors=True)
        os.mkdir(f"{os.getcwd()}/{NDid}Challenge{ChallengeNum}")
    os.system(f"cp -r {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{ChallengeNum}')} {os.getcwd()}/{NDid}Challenge{ChallengeNum}")
    os.system(f"ls -al {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{ChallengeNum}')} >> {os.getcwd()}/{NDid}Challenge{ChallengeNum}/LSOUTPUTS.txt")
    
def RemoveDir(NDid: str, ChallengeNum: str):
    shutil.rmtree(f"{os.getcwd()}/{NDid}Challenge{ChallengeNum}", ignore_errors=True)
    return