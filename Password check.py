def check_password(password):
    if len(password)>=8 and password.isdigit and password.isalpha:
        return "strong"
    elif password.isalpha and len(password)>=8 :
        return "medium"
    elif len(password)>=8:
        return "weak"
    else: return "invalid"

print(check_password("hllllllll"))
