def repeatedNumList(listVals):
    repeated = []                           # A new list to store the values that are repeated
    for i in range(len(listVals)):                # Traverse list
        count = 0                                 # Reset counter for each new number
        for j in range(i+1, len(listVals)):       # Nested loop
            if(listVals[i] == listVals[j]):       # if the value from outer loop is equal to values pointed by inner loop then
                count += 1                        # increase counter of repeatition
        
        if (count > 0 and listVals[i] not in repeated):    # If that specific value in List has repeated occurence and not already in list then
            repeated.append(listVals[i])                   # Store that value only once in new list

    return repeated



list = []
repeated = []
content = int(input("Enter the total number of List"))      # Define how many items will be in list
for i in range(content):                                    # Loop to take input
    val = int(input(f"Enter Value {i+1}: "))                # Store user input in var. (doing i+1 as index starts at 0)
    list.append(val)                                        # Add value to list

repeated = repeatedNumList(list)

print("Original List: ", list)
print("Repeated List: ", repeated)
