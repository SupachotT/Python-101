# ---------- Logical Operations ----------
has_high_income = True
has_good_credit = True
has_criminal_crime = False

if has_good_credit or has_high_income:
    print("Eligaible for loan 1")

if has_high_income and not has_criminal_crime:
    print("Eligaible for loan 2")


# ---------- Comprison Operations ----------
temprature = 30
if temprature > 30:
    print("it is a hot today.")
else:
    print("it is not a hot today.")

name = "f"
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks Good!")


# ---------- Weight Converter Program ----------
weight = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")


# ---------- While Loop ----------
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")