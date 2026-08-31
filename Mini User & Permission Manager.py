users={
    
    "hamid": {
        "age": 22,
        "role": "developer",
        "permissions": ["read", "write"]}
        ,
    "ali": {
        "age": 25,
        "role": "developer python",
        "permissions": ["read"]
    }
    ,
    "hossain":{
        "age":30,
        "role": "developer back end",
        "permissions": ["read","write"]

    }
    ,
    "mohammadreza":{
        "age": 18,
        "role": "admin",
        "permissions": ["write"]
    }
    ,
    "shima":{
        "age": 18,
        "role": "security",
        "permissions": ["write"]
        }
}
def username():
    for name in users:
        print(name)

def user_information():
    name=input("enter name user:").lower().strip()
    print(users[name])

def check_permission():
    name=input("enter name user:").lower().strip()
    permission=input("enter permission:").lower().strip()
    
    if permission in users[name]["permissions"]:
        print("✓ Access Granted")
    else:print("✗ Access Denied")

def add_new_user():
    name_new_user=input("enter name new user:").lower().strip()
    age_new_user=int(input("enter age:"))
    role_new_user=input("enter role:").lower().strip()
    permissions_new_user=input("enter pemissions:").strip().lower().split()
    users[name_new_user]={"age":age_new_user,"role":role_new_user,"permissions":permissions_new_user}

def add_permission():
    name=input("enter name user:").lower().strip()
    print(users[name]["permissions"])
    permission=input("enter permission:").lower().strip()
    users[name]["permissions"].append(permission)  

def remove_permission():
    name=input("enter name user:").lower().strip()
    print(users[name]["permissions"])
    permission=input("enter permission:").lower().strip()
    users[name]["permissions"].remove(permission)  

def remove_user():
    name=input("enter name user:").lower().strip()
    del users[name]

def show_roles():
    roles=set()
    for role in users.values():
        roles.add(role["role"])
    print(roles)


while(True):
    entery=int(input('''
========== USER MANAGER ==========
1. Show users
2. User information
3. Check permission
4. Add user
5. Add permission
6. Remove permission
7. Remove user
8. Show roles 
9. Exit
Choose:'''))

    
    if entery==1:
        username()
    elif entery==2:
        user_information()
    elif entery==3:
       check_permission()
    elif entery==4:
        add_new_user()
    elif entery==5:
        add_permission()
    elif entery==6:
         remove_permission()
    elif entery==7:
        remove_user()
    elif entery==8:
        show_roles()
    elif entery==9:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
