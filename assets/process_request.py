from dbms import users

ID=0
preferences="English"
def is_existing_user(phone):
    existing_users = users.read_users() 
    for i in existing_users:
        if str(phone)==str(i[1]):
            global ID,preferences
            ID=i[0]
            preferences=i[2]
            return True
    return False

language = "English"

def process(message, phone):
    if is_existing_user(phone):
        if preferences=="English":
            if "english" in message:
                users.update_user(user_id=ID,preferences="English")
                return "Language already in English"
            elif "malayalam" in message:
                users.update_user(user_id=ID,preferences="Malayalam")
                return "ഭാഷ മലയാളത്തിലേക്ക് മാറ്റി"
            else:
                return "Good to have you back sir! What would you like to order?<catalogue link>"
        elif preferences=="Malayalam":
            if "english" in message:
                users.update_user(user_id=ID,preferences="English")
                return "Language set to English"
            elif "malayalam" in message:
                users.update_user(user_id=ID,preferences="Malayalam")
                return "നിലവിൽ മലയാളം ഭാഷ"
            else:
                return "തിരിച്ചു വന്നതിൽ സന്തോഷം സാർ! നിങ്ങൾ എന്താണ് ഓർഡർ ചെയ്യാൻ ആഗ്രഹിക്കുന്നത്?<catalogue link>"
    else:
        users.insert_user(number=str(phone), preferences=language)
        return "Welcome to *DROP*, Please type in your language\nEnglish\nMalayalam"
