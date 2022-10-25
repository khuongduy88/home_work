num = float(input("Give me a price: "))

if num>=150:
    print("Total: ",num-50)
elif num>=100:
    print("Total: ",num-25)
elif num>=75:
    print("Total: ",num -15)
else:
    print("Total: ",num)