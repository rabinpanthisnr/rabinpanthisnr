gender=str(input("Enter your gender: "))
level=float(input("Enter your hemoglobin value(g/l): "))

if gender=="male":
    if level< 134:
        print("Your hemoglobin is low!")
    elif level < (134<=level<=167):
            print("Your hemoglobin is normal!")
    else:
            print("Your hemoglobin is high!")

if gender=="female" and 117<=level<=155:
    if level < 117:
         print("Your hemoglobin is low!")
    elif level< (117<=level<=155):
        print("Your hemoglobin is normal!")
    else:
        (print("Your hemoglobin is high! "))