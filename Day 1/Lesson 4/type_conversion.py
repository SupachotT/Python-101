# ---------- Typing Conversion ----------
birthYear = input('Brith year ? ')
age = 2024 - int(birthYear)
print(type(age))
print(age)


weight_kg = input('Weight (Kg): ')
weight_lbs = int(weight_kg) / 0.45
print(weight_lbs)
print("Weight(lbs) is: " + str(weight_lbs) + " lbs.")