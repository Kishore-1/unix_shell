import os

import shutil

import datetime

import socket


# change color to red & green
def print_red(invalid):
    print("\033[31m"+invalid+"\033[0m")
def print_exit(exit):
    print("\033[92m"+exit+"\033[0m")

#clears the screen before shell loop
def clrs():                 
    os.system('cls')

# list Files in Current Directory
def list_cd():              

    file_cd = []
    a_lst = os.listdir()    # gets items in current directory

    #Loop that gets the files one by one
    for item in a_lst:
        #checks the item is file or not
        if os.path.isfile(item):
            file_cd.append(item)
    #prints file in terminal
    if file_cd:
        for item in file_cd:
            print(item)
    else:
        print("No files exists in the current directory")

# list Directories in current path
def list_dir():

    folder_cd = []
    b_lst = os.listdir()

        #Loop that gets the files one by one
    for item in b_lst:
        #checks the item is file or not
        if os.path.isdir(item):
            folder_cd.append(item)
   
    #prints file in terminal
    if folder_cd:
        for item in folder_cd:
            print(item)
    else:
        print("No folders found in this directory")

# getting current time from datetime 
curr_dt =  datetime.datetime.now()

# date - strftime used to convert normal date format required str
def dte():
    return curr_dt.strftime("%d-%b-%Y").lower()    


 
#Unix Like SHELL
def shell():
    
    clrs()

    while (1==1):
        
        command = input("Kishore_Shell> ")

        if command == "list":
            list_cd()
        elif command == "dirs":
            list_dir()
        elif command == "date":
           print(dte())
        elif command == "time":
            print(curr_dt.strftime("%H:%M:%S"))
        elif command == "time -hours":               
            print(curr_dt.hour)                     #.hour - gets only hour part
        elif command == "time -mins":               
            print(curr_dt.minute)                   #.minute - gets only minutes part
        elif command == "time -secs":               
            print(curr_dt.second)                   #.second - gets only seconds part
        

        elif command == "exit":
            print_exit("Shell Exited")
            break
        elif command == "":
            print(command)
        else:
            print_red("\t\t\t**************************** Invalid Command ****************************")

shell() # Shell we created


