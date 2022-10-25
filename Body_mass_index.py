weigh= float(input("input your weigh(kg) :"))
tall = float(input("input your tall(m) :"))

MBI=weigh/(tall**2)

if MBI<16 :
    print("Underweight (Severe thinness)")
elif MBI>=16 and MBI<17:
    print("Underweight (Moderate thinness)")
elif MBI>=17 and MBI<18.5:
    print("Underweight (Mild thinness)")
elif MBI>=18.5 and MBI<25:
    print("Normal range")
elif MBI>=25 and MBI<30:
    print("Overweight (Pre-obese)")
elif MBI>=30 and MBI<35:
    print("Obese(Class I)")
elif MBI>=35 and MBI<40:
    print("Obese(Class II)")
else:
    print("Obese(Class III)")
 