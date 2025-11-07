import random
number=int(input("enter number between 1 to 6:\t"))
nbm=random.randint(1,6)

if nbm==number:
   print("wow that amazing!")
else:
   print(f"no its worng{nbm}")
