list = []                           # Initialising List
content = int(input("Enter the total number of List"))      # Define how many items will be in list
for i in range(content):                                    # Loop to take input
    val = int(input(f"Enter Value {i+1}: "))                # Store user input in var. (doing i+1 as index starts at 0)
    list.append(val)                                        # Add value to list

minVal = list[0]                                            # Assuming Min value of list is at first index
maxVal = list[0]                                            # Assuming Max value of list is at first index
sum = 0
print("\n-----Displaying Result----\n")
for i in range(content):                                    # Loop to print list values
    print("Value ", i+1, ": ", list[i])                     # Display value at specific index. (doing i+1 as index starts at 0 for user visual)
    sum += list[i]                                          # Calculating Sum of ELements
    if(minVal > list[i]):                                   # if current Min is greater than current value
        minVal = list[i]                                    # update min
    if (maxVal < list[i]):                                  # if current Min is less than current value
        maxVal = list[i]                                    # update max

print("\n-----Calculating Sum----\n")
print("Sum of Elements:", sum)
print("\n-----Calculating Min and Max Values in List----\n")
print("Min value:", minVal)
print("Max value:", maxVal)
