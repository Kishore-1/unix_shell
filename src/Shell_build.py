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
        print_red("No files exists in the current directory")

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
        print_red("No folders found in this directory")

# getting current time from datetime 
curr_dt =  datetime.datetime.now()

# date - strftime used to convert normal date format to required str
def dte():
    return curr_dt.strftime("%d-%b-%Y").lower()    

# cat <filename> displays file content
def content(filename):
    if os.path.isfile(filename):
        f1 = open(filename,"r") 
        print(f1.read())
        f1.close()
    else:
        print_red("Invalid File name or File not Exists")

#head returns first part
def head(hname,hindex):
    if os.path.isfile(hname):
        h1 = open(hname,"r") 
        h2=h1.readlines()
        if hindex>len(h2):
            print_red("Line Count exceeds")
        elif hindex<0:
            print(h2[:-hindex])
        else:
            print(h2[:hindex])
        h1.close()
    else:
        print_red("Invalid File name or File not Exists")

#tail returns last part
def tail(tname,tindex):
    if os.path.isfile(tname):
        t1 = open(tname,"r") 
        t2=t1.readlines()
        if tindex>len(t2):
            print_red("Line Count exceeds")
        elif tindex<0:
            print(t2[tindex:])
        else:
            print(t2[-tindex:])
        t1.close()
    else:
        print_red("Invalid File name or File does not exist")

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
            # print(curr_dt.hour,":",curr_dt.minute,":",curr_dt.second)
            
        elif command == "time -hours":               
            print(curr_dt.hour)                     #.hour - gets only hour part
        elif command == "time -mins":               
            print(curr_dt.minute)                   #.minute - gets only minutes part
        elif command == "time -secs":               
            print(curr_dt.second)                   #.second - gets only seconds part

        elif command[:3] == "cat":
            filename = command[4:]

        elif command[:4] == "head":
            command = command.strip()
            hl,hrange,hname = command.split()
            head(hname,int(hrange))

        elif command[:4] == "tail":
            command = command.strip()
            tl,trange,tname = command.split()
            tail(tname,int(trange))      

        elif command == "clear":
            clrs()
        elif command == "exit":
            print_exit("Shell Exited")
            break
        elif command == "":
            print(command)
        else:
            print_red("\t\t\t**************************** Invalid Command ****************************")

shell() # Shell we created

               