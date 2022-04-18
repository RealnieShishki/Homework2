#1
print('задача №1')
i = 0
while i < 4:
    print(i, '0000')
    i += 1
print('-------------')

#2
print('задача №2')
j = 0
i = 0
while i < 11:
    cifra = int(input('введите цифру: '))
    i += 1
    if cifra == 5:
        j += 1
print(j)
print('-------------')

#3
print('задача №3')
i = 1
j = 0
while i < 101:
    j += i
    i += 1
print(j)
print('-------------')

#4
print('задача №4')
i = 1
n = 1
while n < 11:
    i *= n
    n += 1
print(i)
print('-------------')

#5
print('задача №5')
number = input('Введите число: ')
for i in number:
    print(i)
print('-------------')

#6
print('задача №6')
summa = 0
number = input('Введите число: ')
for i in number:
    digit = int(i)
    summa += digit
print(summa)
print('-------------')

#7
print('задача №7')
answer = 1
number = input('Введите число: ')
for i in number:
    digit = int(i)
    answer *= digit
print(answer)
print('-------------')

#8
print('задача №8')
number = input('Введите число: ')
for i in number:
    if i == '5':
        print('Цифра 5 присутствует')
        break
    else:
        print('Цифра 5 отсутствует')
print('-------------')

#9
print('задача №9')
j = 0
number = input('Введите число: ')
for i in number:
    i = int(i)
    if i > j:
        j = i
print(j)
print('-------------')

#10
print('задача №10')
j = 0
number = input('Введите число: ')
for i in number:
    if i == '5':
        j += 1
print('Количество 5 в числе: ', j)
print('-------------')