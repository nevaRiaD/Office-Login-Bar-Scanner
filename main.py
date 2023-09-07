# Jaycee Alipio
# 8/27/2023
# Project: Program that uses clock-in system to check office hours

import datetime
from clockFunctions import *
from fileFunctions import *

# Change path if files are moved
file_directory = r"E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner"
ID_path = r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\ID.txt'
logs = r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\logs'
current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%m-%d-%Y")

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
                    print(f"Clock In Time: {user['Time']}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                    
                else:
                    print(f"Clock Out Time: {user['Time']}")
                    print(f"Total Time: {clockTime(created_file_path, user['Time'])}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                found = True
                break
    
        if not found:
            print("ID not found. You have to be part of the ASMC Board of Directors")
        
if __name__ == "__main__":
    main()