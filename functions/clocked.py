import datetime

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