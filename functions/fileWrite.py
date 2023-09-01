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

