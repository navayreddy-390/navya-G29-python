
H = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kilograms: "))
gender = input("Enter your gender (male/female): ")

the_BMI = W / (H ** 2)
print("BMI Calculated is:", the_BMI)

if the_BMI > 0:
    if gender == 'FEMALE' or gender == 'female':
        if the_BMI <= 15.5:
            print("You are underweight")
        elif the_BMI <= 22:
            print("Congrats! You are healthy")
        elif the_BMI <= 28:
            print("You are overweight")
        else:
            print("You are obese")
    elif gender == 'FEMALE' or gender == 'female':
        if the_BMI <= 15.5:
            print("You are underweight")
        elif the_BMI <= 20:
            print("Congrats! You are healthy")
        elif the_BMI <= 25:
            print("You are overweight")
        else:
            print("You are obese")
    else:
        print("Invalid gender entered., pls enter FEMALE  or MALE" )
else:
    print("Enter valid details")