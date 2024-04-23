priceOfHouse = 1000000
good_credit = False

if (good_credit == True):
    discounts = priceOfHouse * 20 / 100
    afterDiscount = int(priceOfHouse - discounts)
    print("Your credit is good. We discounting your house 20%.")
    print("Total Price is " + str(afterDiscount) + " Bath")
else:
    discounts = priceOfHouse * 5 / 100
    afterDiscount = int(priceOfHouse - discounts)
    print("Your credit is bad. We discounting your house 5%.")
    print("Total Price is " + str(afterDiscount) + " Bath")