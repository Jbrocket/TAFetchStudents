import sys
import os
import shutil

def CreateDir(NDid: str):
    try: 
        os.mkdir(f"{os.getcwd()}/{NDid}Challenge{sys.argv[2]}")
    except FileExistsError:
        shutil.rmtree(f"{os.getcwd()}/{NDid}Challenge{sys.argv[2]}", ignore_errors=True)
        os.mkdir(f"{os.getcwd()}/{NDid}Challenge{sys.argv[2]}")
    os.system(f"cp -r {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{sys.argv[2]}')} {os.getcwd()}/{NDid}Challenge{sys.argv[2]}")
    os.system(f"ls -al {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{sys.argv[2]}')} >> {os.getcwd()}/{NDid}Challenge{sys.argv[2]}/LSOUTPUTS.txt")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 bringFiles <ListofNDIDsSeparatedByComma> <Challenge**NUMBER**>")
        sys.exit(1)
    
    try: 
        fp = open(sys.argv[1], "r")
        for NDid in fp.readlines():
            CreateDir(NDid.strip())
    except FileNotFoundError:
        for NDid in  map(lambda x: x.lower(), sys.argv[1].split(",")):
            CreateDir(NDid.strip())