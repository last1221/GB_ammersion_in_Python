num = 2
k = 0
if 1<num<1000000:
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        print("Простое")
    else:
        print("Не является простым")
else:
    print('Число должно быть больше 1 и меньше 100000')
