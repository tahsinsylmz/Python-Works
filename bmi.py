
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = weight / (height*height)
b = a - (int(a))
bmi = int(a)
if b > 0.5 :
    bmi = bmi +1
else :
    bmi = bmi

if bmi < 18.5 :
    print("Your BMI is " +str(bmi)+ ", you are underweight.")
elif bmi > 18.5 and bmi < 25 :
    print("Your BMI is " +str(bmi)+ ", you have a normal weight.")
elif bmi > 25 and bmi < 30 :
    print("Your BMI is " +str(bmi)+ ", you slightly overweight.")
elif bmi > 30 and bmi < 35 :
    print("Your BMI is " +str(bmi)+ ", you are obese.")
else :
    print("Your BMI is " +str(bmi)+ ", you are clinically obese.")