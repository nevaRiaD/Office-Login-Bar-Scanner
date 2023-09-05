import os
from main import ID_path, formatted_date
from clockFunctions import dateCheck

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