def fileOpen():
    try:
        # Note: Change path when using different system
        with open(r'E:\VScode\Python Learning\barScan\Office-Login-Bar-Scanner\ID.txt', "r", encoding="utf-8") as file:
            id_name_pairs = []
        
            for line in file:
                parts = line.strip().split(" ", 1)  # Split at the first space
                if len(parts) >= 2:
                    id_value = int(parts[0])
                    name_value = parts[1]
                    id_name_pairs.append({"ID": id_value, "Name": name_value}) 
                    
        #for pair in id_name_pairs:
        #    print(f"ID: {pair['ID']}, Name: {pair['Name']}")
    except FileNotFoundError:
        print("This file was not found!")
        
    return id_name_pairs

def main():
    id_name_pairs = fileOpen()
    
    if not id_name_pairs:
        return
    
    while True:
        print("Welcome to the Moorpark ASMC Office Login!")
        search_id = int(input("Enter the ID number to search for (or enter -1 to exit): "))
    
        if search_id == -1:
            print("Exiting the program.")
            break
        found = False
        
        for pair in id_name_pairs:
            if pair["ID"] == search_id:
                print(f"ID: {pair['ID']}, Name: {pair['Name']}")
                found = True
                break
    
        if not found:
            print("ID not found. You have to be part of the ASMC Board of Directors")
        
if __name__ == "__main__":
    main()