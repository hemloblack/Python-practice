emails = ["ali@gmail.com", "sara@yahoo", "admin1@site.ir", "reza@", "@hotmail.com", "hacker.com"]

for index, email in enumerate(emails,start=1):
   
   char=email.find("@")
   if (char != -1 and char!=0):
     cearct=email.find(".",char)
     if (cearct !=-1):
      print(f"Email {index}:{email} ✅ Valid")
     else:
       print(f"Email {index}:{email} ❌ Invalid")
   else:
      print(f"Email {index}:{email} ❌ Invalid")
      continue  
      

  
