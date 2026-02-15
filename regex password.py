import re

while True:
    password = input("Enter password : ")

    pattern = r"^[a-zA-Z0-9_@#!]{8,}$"  

    if re.match(pattern, password):
        if not re.search(r"[=.- ]", password):       
            if re.search(r"[A-Z]", password):       
                if re.search(r"\d", password):       
                    print("✅ Password is strong!")
                else:
                    print("❌ Must include at least one digit.")
            else:
                print("❌ Must include at least one uppercase letter.")
        else:
            print("❌ Password includes forbidden characters (= . - space)")
    else:
        print("❌ Password doesn't match base pattern.")
