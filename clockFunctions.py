import datetime
import re

def clockTime(file_path, clocked_out_time):
    clocked_in_time = None

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if "clocked In" in line:
            match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            if match:
                clocked_in_time = match.group(0)
                
    if clocked_in_time and clocked_out_time:
        clocked_in_seconds = time_to_seconds(clocked_in_time)
        clocked_out_seconds = time_to_seconds(clocked_out_time)
        
        total_seconds = clocked_out_seconds - clocked_in_seconds
        total_time = secondsToHHMMSS(total_seconds)
        
        return total_time
    else:
        pass
    
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
    
def secondsToHHMMSS(total_seconds):
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def time_to_seconds(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        return total_seconds
    except ValueError:
        return None
    