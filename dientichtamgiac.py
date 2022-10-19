import math

a=float(input("nhap do dai canh thu nhat: "))
b=float(input("nhap do dai canh thu hai: "))
c=float(input("nhap do dai canh thu ba: "))

s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))

print("dien tich tam giac la:", area)
