# BMI calc

weight = 63
height = 1.84
bmi = weight / height ** 2

if bmi < 18.0:
    print("Under weight")
elif 18.0 <= bmi <= 24.9:
    print("Normal")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
elif 30.0 <= bmi <= 35.9:
    print("Obese")
else:
    print("Overly Obese")
