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
    
    def on_login(id_input):
        id_name_title_pairs = fileOpen()
        
        if not id_name_title_pairs:
            return
    
        search_id = app.text_widget_value()
        print(search_id)
        
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
    
    app = Window(on_login)
    root.mainloop()
    
if __name__ == "__main__":
    main()