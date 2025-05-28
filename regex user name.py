import re

a = input("Enter username: ")
pattern = r"^[a-zA-Z0-9_]{5,12}$"

if re.match(pattern, a):
    print("✅ Username is valid")
else:
    print("❌ Username is invalid")
