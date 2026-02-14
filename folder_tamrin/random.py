import random
print(random.random())
print(random.randint(1,2))
print(random.randrange(0,10,2))# عدد رندوم بین این 0تا 10  با گام های 2 تایی (یعنی دوتا دوتا میره تا 10 و یکی رو انتخاب میکنه)
colors = ["red", "blue", "green"]
print(random.choices(colors,k=5))#انتخاب از بین ایتم ها مجاز به  تکرار ایتم
print(random.sample(colors,k=3))#انتخاب از بین ایتم ها بدون تکرار ایتم
cards = [1, 2, 3, 4,5]
random.shuffle(cards)# برای بهم زدن ترتیب لیست(بُر زدن لیست)
print(cards)
print(random.uniform(1.3,8.5))#انتخاب عدد رندومه اعشاری
