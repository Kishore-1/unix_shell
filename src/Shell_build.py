# Project-02 #  KISHORE-GEERVANI - Build Unix like shell using python ##

import os
import shutil
import datetime
import socket
import click      #install click library

# change color to Red,Yellow,Green
def print_red(red):
    print("\033[31m"+red+"\033[0m")
def print_ylw(pth,ylw):
    print("\033[93m"+ylw+"\033[0m")
def print_exit(green):
    print("\033[92m"+green+"\033[0m")

#clears the screen before shell loop
def clrs():                 
    click.clear()   # clear of function clears the screen 

# list Files in Current Directory
def list_file():              

    file_cd = []
    file_lst = os.listdir()    # gets items in current directory

    #Loop that gets the files one by one
    for item in file_lst:
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
    dir_lst = os.listdir()

        #Loop that gets the files one by one
    for item in dir_lst:
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

# head -(length) filename     returns from top part  of the file
def head(hname,hindex):   
    if os.path.isfile(hname):
        h1 = open(hname,"r") 
        h2=h1.readlines()
        if hindex>len(h2):
            print_red("Line Count exceeds than in file")
        elif hindex<0:
            print(h2[:-hindex])
        else:
            print(h2[:hindex])
        h1.close()
    else:
        print_red("Invalid File name or File not Exists")

# tail -(length) filename     returns from bottom part  of the file
def tail(tname,tindex): 
    if os.path.isfile(tname):
        t1 = open(tname,"r") 
        t2=t1.readlines()
        if tindex>len(t2):
            print_red("Line Count exceeds than in file")
        elif tindex<0:
            print(t2[tindex:])
        else:
            print(t2[-tindex:])
        t1.close()
    else:
        print_red("Invalid File name or File does not exist")

# pwd - Present Working Directory
def pw_dir():
    print_ylw("Path:      \n", os.getcwd())

# IPconfig
def ip():
    host_name = socket.gethostname()
    ipaddr = socket.gethostbyname(host_name)
    print("\nIPv4 Address. . . . . . . . . . . : ",ipaddr,"\n")

# Remove File
def rmv(f_path):
    if os.path.isfile(f_path):
        os.remove(f_path)
        print("File removed Succesfully")
    else:
        print_red("File not found")

# Truncate file
def trun(e_path):
    if os.path.isfile(e_path): 
        e1 = open(e_path,"w")
        e1.truncate()
        e1.close()
        print("File emptied")
    else:
        print_red("File not found")

#copy file
def cpy(c_src,c_dst):   
    if os.path.isfile(c_src):
        shutil.copy(c_src,c_dst)
        print("File Copied")
    else:
        print("File not found")

#Unix Like SHELL
def shell():
    
    clrs() # Auto clears screen every First time program runs

    while (1==1):
        try:
            command = input("Kishore_Shell> ").strip()

            if command == "list":                           
                list_file()                             # List files

            elif command == "dirs":
                list_dir()                              # List directories

            elif command == "date":
                print(dte())                            # Shows date

            elif command == "time":
                print(curr_dt.strftime("%H:%M:%S"))     # Shows time
                # print(curr_dt.hour,":",curr_dt.minute,":",curr_dt.second)

            elif command == "time -hours":              
                print(curr_dt.hour)                     #.hour - gets only hour part
            elif command == "time -mins":               
                print(curr_dt.minute)                   #.minute - gets only minutes part
            elif command == "time -secs":               
                print(curr_dt.second)                   #.second - gets only seconds part

            elif command[:3] == "cat":                  # cat shows file content
                if len(command.split()) == 2:
                    filename = command.split()[1]
                    content(filename)
                else:
                    print_red("invalid command missing length or path")

            elif command[:4] == "head":                 # head shows top lines
                if (len(command.split()) == 3):
                    hrange,hname = command.split()[1:]
                    head(hname,int(hrange))
                else:
                    print_red("invalid command missing length or path")

            elif command[:4] == "tail":   
                if len(command.split()) == 3:              # tail shows bottom lines
                    trange,tname = command.split()[1:]
                    tail(tname,int(trange)) 
                else:
                    print_red("invalid command missing length or path")

            elif command[:11] == "remove_file":         # removes file 
                if len(command.split()) == 2:
                    f_path = command.split()[1]
                    rmv(f_path)
                else:
                    print_red("invalid command - missing path/Filename")

            elif command[:10] == "empty_file":          # truncates file
                if len(command.split()) == 2:
                    e_path = command.split()[1]
                    trun(e_path)
                else:
                    print_red("invalid command - missing path/Filename")

            elif command[:9] == "copy_file":            # copies file 
                if len(command.split()) == 3:
                    c_src = command.split()[1]
                    c_dst = command.split()[2]
                    cpy(c_src,c_dst)
                else:
                    print_red("invalid command - missing src/dest")

            elif command == "pwd":                     # present working directory get_cwd
                pw_dir()  

            elif command == "ipconfig":                # shows ip address
                ip()

            elif command == "clear":                   # clear screen
                clrs()
            elif command == "":
                print(command)                         # loops again to get shell command

            elif command == "exit":
                print_exit("Shell Exited")             # exits shell 
                break
            else:
                print_red("\t\t\t**************************** Invalid Command ****************************")

        except Exception as e:
            print(f"unexpected Error: {e}")

shell() # Shell created


###################### THANK YOU !!! ############################################ THANK YOU !!! ############################################ THANK YOU !!! ######################

               
