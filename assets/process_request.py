from dbms import users

def is_existing_user(phone):
    existing_users = users.read_users() 
    for i in existing_users:
    	if str(phone)==str(i[1]):
    		return True
    return False

language = "English"

def process(message, phone):
    if is_existing_user(phone):
        return "Good to have you back sir! What would you like to order?"
    else:
        users.insert_user(number=str(phone), preferences=language)
        return "Welcome to *DROP*, Please choose your language\n1. English\n2. Malayalam"
