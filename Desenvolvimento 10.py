class numComplexo:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def __str__(self):
        return "{} + {}i".format(self.real,self.img)
    
    def __add__(self,num):
        real = self.real + num.real
        img = self.img + num.img
        return numComplexo(real,img)
    
    def __sub__(self,num):
        real = self.real - num.real
        img = self.img - num.img
        return numComplexo(real,img)

    def __mul__(self,num):
        a = self.real
        b = self.img
        c = num.real
        d = num.img
        real = a*c - b*d
        img = a*d + b*c
        return numComplexo(real,img)

    def __truediv__(self,num):
        a = self.real
        b = self.img
        c = num.real
        d = num.img
        real = (a*c - b*d) / (c**2 + d**2)
        img = (a*d + b*c) / (c**2 + d**2)
        return numComplexo(real,img)

import random
x = numComplexo(random.randint(1, 99), random.randint(1, 99))
y = numComplexo(random.randint(1, 99), random.randint(1, 99))

adicao = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y

print("Número 1:",x)
print("Número 2:",y)
print()
print("Soma:",adicao)
print("Subtração:",subratacao)
print("Multiplicação:",multiplicacao)
print("Divisão:",divisao)
