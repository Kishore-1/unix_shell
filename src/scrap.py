import os



def tail(path,tindex):
    if os.path.isfile(path):
        t1 = open(path,"r") 
        t2=t1.readlines()
        range = t2[tindex:]
        print(range)
        t1.close()

    else:

        print("Invalid File name or File does not exist")


command = input("enter> ").strip()
if command[:4] == "tail":
    nm,trange,path = command.split()
    tindex=int(trange)
    tail(path,tindex)


