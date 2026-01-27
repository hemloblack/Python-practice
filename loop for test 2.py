numbers = [12, 7, 5, 64, 14, 9, 22, 3, 18, 27, 33, 41, 60, 90, 1,5]
even = []
big_even = []
odd = []
small_odd_squares = []
majmoeodd = 0

for i in numbers:
    if i % 2 == 0:
        even.append(i)
        if i > 20:
            big_even.append(i)
    elif i < 30:
        odd.append(i)
        small_odd_squares.append(i * i)#محاسبه مربع عداد داخل لیست  
        majmoeodd += i

if len(small_odd_squares) > 0:#برسی خالی یا خالی نبودن لیست
    average = majmoeodd / len(small_odd_squares)
else:
    average = 0

print(even)
print(big_even)
print(odd)
print(small_odd_squares)
print(majmoeodd)
print(average)
