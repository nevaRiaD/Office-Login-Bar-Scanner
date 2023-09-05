# Jaycee Alipio
# 8/27/2023
# Project: Program that uses clock-in system to check office hours

import tkinter as tk
from tkinter import filedialog, Text
from tkinter import ttk

import datetime
import os
import re

# Change path if files are moved
ID_path = r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\ID.txt'
logs = r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\logs'
current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%m-%d-%Y")

# Opens file to search through list
def fileOpen():
    try:
        with open(ID_path, "r", encoding="utf-8") as file:
            id_name_title_pairs = []
        
            for line in file:
                parts = line.strip().split(" ", 2)
                if len(parts) >= 3:
                    id_value = int(parts[0])
                    name_value = parts[1]
                    role_value = parts[2]
                    id_name_title_pairs.append({"ID": id_value, "Name": name_value, "Role": role_value, "Status": "Out", "Time": None}) 

    except FileNotFoundError:
        print("This file was not found!")
        
    return id_name_title_pairs

def fileCreate(directory, file_name, name):
    try:
        file_create_name = str(file_name) + " " + name.replace('_', ' ') + ".txt"
        file_path = os.path.join(directory, file_create_name)
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                # File is created here
                print(f"File '{file_path}' has been created.")
                return file_path
        else:
            return file_path
    except FileExistsError:
        pass
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None

def fileWrite(file_path, name ,time, status):
    try:
        name = name.replace('_', ' ')
        if not dateCheck(file_path):
                with open(file_path, "a") as file:
                    file.write(f"\n{formatted_date}\n")
                    
        with open(file_path, "a") as file: 
            file.write(f"- {name} clocked {status} at {time}\n")
            
        print(f"Log has been recorded to '{file_path}' successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def dateCheck(file_path):
    try:
        last_date = None
        
        with open(file_path, "r") as file:
            lines = file.readlines()
            
            for line in reversed(lines):
                line = line.strip()
                try:
                    last_date = datetime.datetime.strptime(line, "%m-%d-%Y").date()
                    break
                except ValueError:
                    continue
        
        if last_date and last_date == datetime.date.today():
            return True
        else:
            return False
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def idFound(user, name, role):
    name = name.replace('_', ' ')
    role_clock_in_behaviors = {
        "President": "Clocked In",
        "Vice President": "Clocked In",
        "Director of Academic Affairs": "Clocked In",
        "Director of Budget and Finance": "Clocked In",
        "Director of Campus Events": "Clocked In",
        "Director of Constitution and Standing Rules": "Clocked In",
        "Director of Public Relations": "Clocked In",
        "Director of Student Advocacy": "Clocked In",
        "Director of Student Organization": "Clocked In",
        "Director of Student Services": "Clocked In",
        "Director of Sustainability": "Clocked In",   
    }

    clock_in_behavior = role_clock_in_behaviors.get(role, "Clocked In") # Default to "Clocked In" if role not found
    status = user["Status"]
    
    if status == "Out":
        check = str(input(f"Would you like to clock in for {name}? [yes] [no] : "))
        if check == "yes":
            user["Status"] = "In"
            user["Time"] = datetime.datetime.now().strftime("%H:%M:%S")
            return "In"
        else:
            pass
    else:
        check = str(input(f"Would you like to clock out {name}? [yes] [no] : "))
        if check == "yes":
            user["Status"] = "Out"
            user["Time"] = datetime.datetime.now().strftime("%H:%M:%S")
            
            return "Out"
        else:
            pass

def time_to_seconds(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        return total_seconds
    except ValueError:
        return None

def secondsToHHMMSS(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def clockTime(file_path):
    clocked_in_time = None
    clocked_out_time = None
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if "clocked In" in line:
            match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            if match:
                clocked_in_time = match.group(0)
        elif "clocked Out" in line:
            match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            if match:
                clocked_out_time = match.group(0)
                
    if clocked_in_time and clocked_out_time:
        clocked_in_seconds = time_to_seconds(clocked_in_time)
        clocked_out_seconds = time_to_seconds(clocked_out_time)
        
        total_seconds = clocked_out_seconds - clocked_in_seconds
        total_time = f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}"
        
        return total_time
    else:
        pass

def main():
    id_name_title_pairs = fileOpen()
    
    if not id_name_title_pairs:
        return
    
    while True:
        print("\nWelcome to the Moorpark ASMC Office Login!")
        search_id = int(input("Enter the ID number to search for (or enter -1 to exit): "))
    
        if search_id == -1:
            print("Exiting the program.")
            break
        found = False
        
        for user in id_name_title_pairs:
            if user["ID"] == search_id:
                status = idFound(user, user["Name"], user["Role"])
                print(f"\nUser: {user['Name'].replace('_', ' ')} (ID: {user['ID']})")
                print(f"Role: {user['Role'].replace('_', ' ')}")
                print(f"Status: Clocked {status}")
                print(f"Date: {formatted_date}")
                
                created_file_path = fileCreate(logs, user["ID"], user["Name"])
                
                if status == "In":
                    print(f"Clocked In Time: {user['Time']}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                    
                else:
                    print(f"Clocked Out Time: {user['Time']}")
                    print(f"Total Time: {clockTime(created_file_path)}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                found = True
                break
    
        if not found:
            print("ID not found. You have to be part of the ASMC Board of Directors")
        
root = tk.Tk()

canvas = tk.Canvas(root, height = 600, width = 900, bg="#020079")
canvas.pack()

frame = tk.Frame(root, bg="#020079")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

if __name__ == "__main__":
    main()