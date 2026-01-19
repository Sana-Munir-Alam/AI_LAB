dict = {}

dict['name'] = input("Enter Your Name:")    # Display message and store user Value in dict
dict['age'] = input("Enter Your Age:")      # Display message and store user Value in dict
dict['city'] = input("Enter Your City:")    # Display message and store user Value in dict

print('\n===== Created Dictionary ===== \n Dictionary Output: ', dict)
print("\n\nDisplaying Output: Name: ", dict['name'], ", Age:", dict ['age'], ", City:", dict ['city'])

# Check Eligibility criteria
if dict['age'] >= '18':                     # NOte: Compare string with string, and int with int never mix these two
    print("Eligible For Vote")
else:
    print("Not Eligible For Vote")
