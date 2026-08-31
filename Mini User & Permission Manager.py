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
        "role": "developer python",
        "permissions": ["read","write"]

    }
    ,
    "mohammadreza":{
        "age": 18,
        "role": "developer",
        "permissions": ["write"]
    }
    ,
    "shima":{
        "age": 18,
        "role": "developer",
        "permissions": ["write"]
        }
}

while(True):
    entery=int(input("========== USER MANAGER ==========\n1. Show users\n2. User information\n3. Check permission\n4. Add user\n5. Add permission\n6. Remove permission\n7. Remove user\n8. Show roles \n9. Exit\nChoose:"))
    if entery==1:
        print(users.keys())
    if entery==2:
        name=input("enter name user:").lower().strip()
        print(users[name])
    if entery==3:
        name=input("enter name user:").lower().strip()
        permission=input("enter permission:").lower().strip()
        permissions=users[name].get("permissions")
        if permission in permissions:
            print("✓ Access Granted")
        else:print("✗ Access Denied")
    if entery==4:
        name_new_user=input("enter name new user:").lower().strip()
        age_new_user=int(input("enter age:"))
        role_new_user=input("enter role:").lower().strip()
        permissions_new_user=input("enter pemissions:").strip().lower().split()
        users[name_new_user]={"age":age_new_user,"role":role_new_user,"permissions":permissions_new_user}
    if entery==5:
        name=input("enter name user:").lower().strip()
        permission=input("enter permission:").lower().strip()
        users[name].update({"permissions":permission})
    if entery==6:
         name=input("enter name user:").lower().strip()
         
         del users[name]["permissions"]
         print(users[name].get("permissions"))
    if entery==7:
        name=input("enter name user:").lower().strip()
        del users[name]
    if entery==8:
        name=input("enter name user:").lower().strip()
        role=set
        role=users[name]["role"]
        print(role)
        print(type(role))
