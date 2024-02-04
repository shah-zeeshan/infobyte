
def info():
    print("****************BMI Calculator****************")
    name_info = input("Please enter your name here: ")
    weight_info = float(input("{}, Enter your weight in kilograms (kg) :  ".format(name_info)))
    height_info = float(input("{}, Ynter your height in meters (m):  ".format(name_info)))
    check_bmi(height_info, weight_info, name_info)

def check_bmi(height,weight,name):
    bmi = weight/(height*height)
    if bmi<18.5:
        print("\nYou are under weight")
    elif 18.5< bmi <=24.9:
        print("\nYou have normal weight")
    elif 25<=bmi<=29.9:
        print("\nYou are Overweight")
    else:
        print("\nYou are Obese")

    print("\n{}, your BMI is {}".format(name, bmi))
    print("\n*****Healthy Measures*****.\n ~Learn more about overweight and obesity.\n ~Increase Physical Activity.\n ~Moving more can lower your risk factors for heart disease.\n ~Eat a Heart-Healthy Diet Eating a healthy diet is the key to heart disease prevention.")



info()
