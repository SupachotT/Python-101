# ---------- Logical Operations ----------
has_high_income = True
has_good_credit = True
has_criminal_crime = False

if has_good_credit or has_high_income:
    print("Eligaible for loan 1")

if has_high_income and not has_criminal_crime:
    print("Eligaible for loan 2")