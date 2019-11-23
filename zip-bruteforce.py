#!/usr/bin/env python3

from zipfile import ZipFile
import argparse


BLUE = "\033[34m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"
RESET = "\033[0;0m"
YELLOW = "\033[33m"


print(BLUE + """\n\n
               +------------------------------------------------+
               |                  Coded by : L                  |
               |                                                |
               | https://github.com/shellbr3ak?tab=repositories |
               +------------------------------------------------+
                ____  _          _ _ ____                 _    
               / ___|| |__   ___| | | __ ) _ __ ___  __ _| | __
               \___ \| '_ \ / _ \ | |  _ \| '__/ _ \/ _` | |/ /
                ___) | | | |  __/ | | |_) | | |  __/ (_| |   < 
               |____/|_| |_|\___|_|_|____/|_|  \___|\__,_|_|\_|
                                                                                          
                                offensive python                
                                ----------------


""" + RESET)


parser = argparse.ArgumentParser(description="Usage: python3 zip-bruteforce.py -z <zipfile.zip> -p <passwordfile.txt>")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="Password file")
parsed_args = parser.parse_args()

try:
    ziparchive = ZipFile(parsed_args.ziparchive)
    passfile = parsed_args.passfile
    foundpass = ""

except:
    print(RED + parser.description + RESET)
    exit(0)

with open(passfile, "r") as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode("utf-8")

        try:
            foundpass = ziparchive.extractall(pwd=password) #pwd= password from the file in the current line
            if foundpass == None: # the archive was extracted successfully
                print("Found password :" + GREEN + f"{password.decode()}" + RESET)
        except RuntimeError: #in case the password was wrong the extractall() will throw an error
            pass
    if foundpass == "":
        print(RED + "Password Not Found, Try a bigger password list." + RESET)
