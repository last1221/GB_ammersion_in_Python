a = 4
b = 2
c = 3

if a+b>c and a+c>b and b+c>a:
    print('Треугольник существует')
    if a==b==c:
        print('Треугольник равносторонний')
    elif a==b!=c or b==c!=a or a==c!=b:
        print('Треугольник равнобедренный')
    elif a!=b!=c:
        print('Треугольник разносторонний')

else:
    print('Треугольник не существует')