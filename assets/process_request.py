from dbms import users
import json

users_data = {}

def add_or_edit_user(phone, user_id, user_preferences):
    if phone in users_data:
        # Edit existing user
        users_data[phone]["id"] = user_id
        users_data[phone]["preferences"] = user_preferences
        return "User data updated successfully."
    else:
        # Add new user
        users_data[phone] = {"id": user_id, "preferences": user_preferences}
        return "User added successfully."

def is_existing_user(phone):
    existing_users = users.read_users() 
    for i in existing_users:
        if str(phone)==str(i[1]):
            add_or_edit_user(phone,i[0],i[2])
            return True
    return False

language = "English"

def process(message, phone):
    if is_existing_user(phone):
        if users_data[phone]['preferences']=="English":
            if "english" in message:
                users.update_user(user_id=users_data[phone]["id"],preferences="English")
                return "Language already in English"
            elif "malayalam" in message:
                users.update_user(user_id=users_data[phone]["id"],preferences="Malayalam")
                return "ഭാഷ മലയാളത്തിലേക്ക് മാറ്റി"
            else:
                return "Good to have you back sir! What would you like to order?<catalogue link>"
        elif users_data[phone]['preferences']=="Malayalam":
            if "english" in message:
                users.update_user(user_id=users_data[phone]["id"],preferences="English")
                return "Language set to English"
            elif "malayalam" in message:
                users.update_user(user_id=users_data[phone]["id"],preferences="Malayalam")
                return "നിലവിൽ മലയാളം ഭാഷ"
            else:
                return "തിരിച്ചു വന്നതിൽ സന്തോഷം സാർ! നിങ്ങൾ എന്താണ് ഓർഡർ ചെയ്യാൻ ആഗ്രഹിക്കുന്നത്?<catalogue link>"
    else:
        users.insert_user(number=str(phone), preferences=language)
        is_existing_user(phone)
        return "Hi, "+str(phone)+"Welcome to *DROP*, Please type in your language\nEnglish\nMalayalam"
