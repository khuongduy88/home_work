#input number what you want to check
c = float(input("input your integer : "))

while c<=0 or c % 1 != 0:
    c=float(input("your number is not integer, try again! : "))

mes = "Even"if c%2==0 else "Odd"
print("your number is : "+mes)
