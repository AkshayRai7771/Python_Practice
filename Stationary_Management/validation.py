import re
def is_valid_email(email):
    alert  = "Please Enter Valid Mail !!"
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True
    else:
        print("Please enter a valid mail !!")
        return False
    


    


