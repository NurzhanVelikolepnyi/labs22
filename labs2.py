import datetime  #1 modultask
now = datetime.datetime.now()
print ("Текущая дата и время: ", now.strftime("%Y-%m-%d %H:%M:%S"))

import datetime  #2modultask
now = datetime.datetime.now()

name = input("как вас зовут?")
age = int (input ("Cколько вам лет?"))
year = str((now.year - age) + 100)
print(name + ", Baм будет 100 лет в"  + year + " году")


def fib(n): #3modultask
	a, b = 0, 1
	while b < n:
		print(b, end=' ')
		a, b = b, a+b
	print()


import math  #4

import math as m    # Создание псевдонима
print (m.pi)



import pprint  #5modultask
def countLetters(word):
    y = {}
    for i in word:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    return y

res1 = countLetters("Некоторое значение")
pprint.pprint(res1)

res2 = countLetters("23.4")
pprint.pprint(res2)