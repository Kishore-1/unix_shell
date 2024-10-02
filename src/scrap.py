import os

def content(filename):
    if os.path.isfile(filename):
        f1 = open(filename,"r") 
        print(f1.read())
        f1.close()

# content("File1")
# content(r"C:\Users\kimuruga\Desktop\pro_shell\film.txt")

command = input().strip()
# print(command[0:3],command[3:])
if command[:3] == "cat":
    filename = command[4:]
    content(filename)
else:
    print("invalid file Name")

