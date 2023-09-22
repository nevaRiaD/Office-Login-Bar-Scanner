import datetime, os
from functions.clockFunctions import *
from functions.fileFunctions import *
from functions.GUI import *

# Change path if files are moved
main_directory = os.path.dirname(__file__)
ID_path = main_directory + "\ID.txt"
logs_path = main_directory + "\logs"
current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%m-%d-%Y")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    root.resizable(False, False)
    app = Window()
    root.mainloop()
    
    #app.function1()
    
    id_name_title_pairs = fileOpen()
    
    if not id_name_title_pairs:
        return
    
    while True:
        search_id = app.text_widget_value()
    
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
                
                created_file_path = fileCreate(logs_path, user["ID"], user["Name"])
                
                if status == "In":
                    print(f"Clock In Time: {user['Time']}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                    
                else:
                    print(f"Clock Out Time: {user['Time']}")
                    print(f"Total Time: {clockTime(created_file_path, user['Time'])}")
                    fileWrite(created_file_path, user["Name"], user["Time"], status)
                found = True
                break
    
        #if not found:
        #    print("ID not found. You have to be part of the ASMC Board of Directors")
        
if __name__ == "__main__":
    main()