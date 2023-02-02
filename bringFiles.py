import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 bringFiles <ListofNDIDsSeparatedByComma> <Challenge**NUMBER**>")
        sys.exit(1)
    
    try: 
        fp = open(sys.argv[1], "r")
        for NDid in fp.readlines():
            os.system(f"cp -r {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{sys.argv[2]}')} {os.getcwd()}/{NDid}Challenge{sys.argv[2]}")
    except FileNotFoundError:
        lowered_list = map(lambda x: x.lower(), sys.argv[1].split(","))
        for NDid in lowered_list:
            os.system(f"cp -r {os.path.expanduser(f'~/esc-courses/sp23-cse-20312.01/dropbox/{NDid}/*{sys.argv[2]}')} {os.getcwd()}/{NDid}Challenge{sys.argv[2]}")
