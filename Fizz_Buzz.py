import math as m

a = int(input("input start number : "))
b = int(input("input end number : "))

while a>b:
    print("your number is error! please try again for start < end ")
    a = int(input("input start number : "))
    b = int(input("input end number : "))
    break

for i in range(a,b):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end =" ")
    elif i%3 ==0 and i%5!=0:
        print("Fizz",end =" ")
    elif i%5 ==0 and i%3!=0:
        print("Buzz",end =" ")
    else:
        print(i,end = " ")
 
        