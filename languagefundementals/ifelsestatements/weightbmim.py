weight_kg = int(input("enter weight in kg? "))
height_in_cm = int(input("enter height in cm? "))
height_in_m = height_in_cm/100
bmi = weight_kg/height_in_m **2
if bmi <19:
    print("you are under weight")
elif bmi< 25:
    print("you are healthy")
elif bmi < 30:
    print("you are overweight")
elif bmi < 40:
    print("you are obese")
else:
    print("you are sever obese")