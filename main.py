# Jaycee Alipio
# 8/27/2023
# Project: Clock in system that checks text file

import datetime

# Opens file to search through list
def fileOpen():
    try:
        # Note: Change path when using different system
        with open(r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\ID.txt', "r", encoding="utf-8") as file:
            id_name_title_pairs = []
        
            for line in file:
                parts = line.strip().split(" ", 2)  # Split at the first space
                if len(parts) >= 3:
                    id_value = int(parts[0])
                    name_value = parts[1]
                    role_value = parts[2]
                    id_name_title_pairs.append({"ID": id_value, "Name": name_value, "Role": role_value, "Status": "Out", "Time": None}) 

    except FileNotFoundError:
        print("This file was not found!")
        
    return id_name_title_pairs

def fileWrite():
    print("Awesome")

# Attach a status of clocked in/out while attaching time
def idFound(user, name, role):
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
        user["Status"] = "In"
        user["Time"] = datetime.datetime.now().strftime("%H:%M:%S")
        return "In"
    else:
        user["Status"] = "Out"
        user["Time"] = datetime.datetime.now().strftime("%H:%M:%S")
        return "Out"

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
                print(f"User: {user['Name']} (ID: {user['ID']})")
                print(f"Role: {user['Role']}")
                print(f"Status: Clocked {status}")
                if status == "In":
                    print(f"Clocked In Time: {user['Time']}")
                else:
                    print(f"Clocked Out Time: {user['Time']}")
                found = True
                break
    
        if not found:
            print("ID not found. You have to be part of the ASMC Board of Directors")
        
if __name__ == "__main__":
    main()