
frac1 = "1/2".rsplit('/')
frac2 = "1/3".rsplit('/')

a = int(frac1[0])
b = int(frac1[1])
c = int(frac2[0])
d = int(frac2[1])

m=a*d+b*c
n=d*b
c=m
d=n
while m != 0 and n != 0:
    if m > n:
        m = m % n
    else:
        n = n % m
if m != 0:
    print(f"Сумма дробей: {c // m}/ {d // m}")
else:
    print(f"Сумма дробей: {c // n}/{d // n}")





