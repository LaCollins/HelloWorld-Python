weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    weight = float(weight) * 2.20462
    print("Weight in Lbs:", weight)
elif unit.upper() == "L":
    weight = float(weight) * 0.453592
    print("Weight in Kgs:", weight)
