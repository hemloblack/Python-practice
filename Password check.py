def is_positive(number):
    if  not number>=0:
        return "not correct! please again",False
    else:
        return "that`s correct ",True 
        

num=int(input("enter number between 1,..."))
print(is_positive(num))
        
        