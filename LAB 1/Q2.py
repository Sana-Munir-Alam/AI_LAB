string_test = input("Enter any String you want: ")

print("First Character: ", string_test[0])
print("Last Character: ", string_test[len(string_test) - 1])        # Calculate total length of string -1 (to remove the string terminator)
print("Length of String: ", len(string_test))                       # Subtract 1 because of index starting at 0, so the last character is at index length − 1.
print("Repeated Twice String: ", string_test * 2)                   # Print string two times

count = 0                                                           # Counter to Calculate No.of characters excluding space.
for ch in string_test:                                              # Traverse  the string starting from 0. (Automatcially increments)
    if (ch != " "):                                                 # Condition check if current character is not space
        count += 1                                                  # Increment counter
print("No. of Characters without space: ", count)                   # Printing total number of characters
