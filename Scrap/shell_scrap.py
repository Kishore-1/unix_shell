import os

import shutil

import datetime

import socket

def list_cd():   
# list directories
    file_cd = []
    a_lst = os.listdir()    # gets items in current directory

#Loop
    for item in a_lst:
        if os.path.isfile(item):
            file_cd.append(item)

    if file_cd:
        for item in file_cd:
            print(item)
    else:
        print("No files exists in the current directory")

def shell():
    while (1==1):
        command = input("Kishore_Shell> ")

        if command == "list":
            list_cd()
        else:
            print("Invalid command")

if __name__ == "__main__":
    shell()
