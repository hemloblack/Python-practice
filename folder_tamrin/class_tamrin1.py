# 🎯 تمرین:

# کلاسی بساز به اسم Car که:

# رنگ (color)

# مدل (model)
# داشته باشه
# و یک متد به اسم info که مشخصات رو چاپ کنه.

class car:# کلاسی بساز به اسم Car که:
    def __init__(self,color,model):
        self.color=color# رنگ (color)
        self.model=model# مدل (model)
    def info(self):# و یک متد به اسم info که مشخصات رو چاپ کنه.
        print("car name is ",self.model,"and color car",self.color)

p=car("red","bmw")
p.info()

