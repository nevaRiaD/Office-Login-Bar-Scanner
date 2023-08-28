def fileOpen():
    try:
        # Note: Change path when using different system
        with open(r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\ID.txt', "r", encoding="utf-8") as file:
            id_name_pairs = {}
        
            for line in file:
                parts = line.strip().split(" ", 1)  # Split at the first space
                if len(parts) >= 2:
                    id_value = int(parts[0])
                    name_value = parts[1]
                    id_name_pairs[id_value] = name_value       
                    
        for id, name in id_name_pairs.items():
            print(f"ID: {id}, Name: {name}")
    except FileNotFoundError:
        print("This file was not found!")
fileOpen()