import os

import shutil

import datetime

import socket


# Listing files that reside in currrent directory
def list_files():

  try:

    for item in os.listdir():

      if os.path.isfile(item):

        print(item)

  except Exception as e:

    print(f"Error listing files: {e}")


# Listing directories that reside in currrent directory
def list_dirs():

  try:

    for item in os.listdir():

      if os.path.isdir(item):

        print(item)

  except Exception as e:

    print(f"Error listing directories: {e}")



def system_date():

  try:

    print(datetime.datetime.now().strftime("%d-%b-%Y").lower())

  except Exception as e:

    print(f"Error displaying date: {e}")



def system_time():

  try:

    print(datetime.datetime.now().strftime("%H:%M:%S"))

  except Exception as e:

    print(f"Error displaying time: {e}")



def time_hours():

  try:

    print(datetime.datetime.now().strftime("%H"))

  except Exception as e:

    print(f"Error displaying hours: {e}")



def time_minutes():

  try:

    print(datetime.datetime.now().strftime("%M"))

  except Exception as e:

    print(f"Error displaying minutes: {e}")



def time_seconds():

  try:

    print(datetime.datetime.now().strftime("%S"))

  except Exception as e:

    print(f"Error displaying seconds: {e}")



def cat(filename):

  try:

    with open(filename, 'r') as file:

      print(file.read())

  except Exception as e:

    print(f"Error reading file: {e}")



def head(filename, lines=5):

  try:

    with open(filename, 'r') as file:

      for _ in range(lines):

        print(file.readline(), end="")

  except Exception as e:

    print(f"Error reading file: {e}")



def tail(filename, lines=5):

  try:

    with open(filename, 'r') as file:

      all_lines = file.readlines()

      for line in all_lines[-lines:]:

        print(line, end="")

  except Exception as e:

    print(f"Error reading file: {e}")



def copy_file(src, dest):

  try:

    shutil.copy(src, dest)

    print(f"Copied {src} to {dest}")

  except Exception as e:

    print(f"Error copying file: {e}")



def remove_file(filename):

  try:

    os.remove(filename)

    print(f"{filename} removed successfully.")

  except Exception as e:

    print(f"Error removing file: {e}")



def empty_file(filename):

  try:

    open(filename, 'w').close()

    print(f"{filename} has been truncated.")

  except Exception as e:

    print(f"Error truncating file: {e}")



def ipconfig():

  try:

    hostname = socket.gethostname()

    ip_address = socket.gethostbyname(hostname)

    print(f"IP Address: {ip_address}")

  except Exception as e:

    print(f"Error retrieving IP address: {e}")



def pwd():

  try:

    print(os.getcwd())

  except Exception as e:

    print(f"Error displaying current directory: {e}")



def clear_screen():

  os.system('cls' if os.name == 'nt' else 'clear')



def exit_shell():

  print("Exiting shell...")

  exit()



def shell():

  commands = {

    "list": list_files,

    "dirs": list_dirs,

    "date": system_date,

    "time": system_time,

    "time-hours": time_hours,

    "time-mins": time_minutes,

    "time-secs": time_seconds,

    "ipconfig": ipconfig,

    "pwd": pwd,

    "clear": clear_screen,

    "exit": exit_shell

  }



  while True:

    try:

      command = input("Kishore> ").strip().split()

      if len(command) == 0:

        continue

      elif command[0] in commands:

        commands[command[0]]()

      elif command[0] == "cat" and len(command) == 2:

        cat(command[1])

      elif command[0] == "head" and len(command) == 3 and command[1] == "-5":

        head(command[2], 5)

      elif command[0] == "tail" and len(command) == 3 and command[1] == "-5":

        tail(command[2], 5)

      elif command[0] == "copy_file" and len(command) == 3:

        copy_file(command[1], command[2])

      elif command[0] == "remove_file" and len(command) == 2:

        remove_file(command[1])

      elif command[0] == "empty_file" and len(command) == 2:

        empty_file(command[1])

      else:

        print(f"Invalid command: {' '.join(command)}")

    except Exception as e:

      print(f"An error occurred: {e}")



if __name__ == "__main__":

  shell()

