def DiscountFunction(amount):                # Fucntion that takes "amount" as parameter
    if (amount < 1000):
        amount -= (amount * 0.05)            # 5% discount added Amount = Amount - (Amount * 5/100)
    elif (amount < 5000):
        amount -= (amount * 0.1)             # 10% discount added Amount = Amount - (Amount * 10/100)
    else:
        amount -= (amount * 0.15)            # 15% discount added Amount = Amount - (Amount * 15/100)
    return amount                            # returns net payable amount after discount applied

netPayable = DiscountFunction(970)           # For 5%     => Amount = 970 - (970 * 0.05) = 921.5
print(f"Discounted Price (5% off) on $970: ${netPayable}")
netPayable = DiscountFunction(4520)          # For 10%    => Amount = 4520 - (4520 * 0.1) = 4068
print(f"Discounted Price (10% off) on $4520: ${netPayable}")
netPayable = DiscountFunction(7845)          # For 15%    => Amount = 7845 - (7845 * 0.15) = 6668.25
print(f"Discounted Price (15% off) on $ 7845: ${netPayable}")
