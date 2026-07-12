#BMI calculator
#Input
number = ".0123456789"
finish = False
#Procces
while not finish:
    weight_no = False
    height_no = False
    w = input("Enter your weight in Kg or done to finish: ")
    if w == "done":
        finish = True
    else:
        m = input("Enter your height in m: ")
        for c in w:
            if not c in number:
                print ("Not a valid weight")
                weight_no = True
        for c in m:
            if not c in number:
                print ("Not a valid height")
                height_no = True
        if not weight_no and not height_no:
            w = float(w)
            m = float(m)
            BMI = w/(m*m)
#Output
            if BMI < 18.5:
                print(f"BMI: {BMI:} — Underweight")
            elif 18.5 <= BMI < 25:
                print(f"BMI: {BMI:} — Normal")
            elif 25 <= BMI < 30:
                print(f"BMI: {BMI: — Overweight")
            elif BMI >= 30:
                print(f"BMI: {BMI:} — Obese")