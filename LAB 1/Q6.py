def longestSubstring(string):                # Function that takes string as a parameter
    longestSubstring = ""
    currentSubstring = ""
    for ch in string:
        if (ch not in currentSubstring):                        # check if current Character doenst exist in currentSubstring
            currentSubstring += ch                              # Appending the new character in the currentSubstring if TRUE
        else:                                                   # Means Character already exist so repeatition
            index = 0                                           # FInd the index where the first occurence of that char existed in CurrSubstring
            for i in range(len(currentSubstring)):
                if (ch == currentSubstring[i]):
                    index = i                                   # store that index value
                    break
            currentSubstring = currentSubstring[index+1:] + ch  # Concatinate from after the original char (which got repeated)
        if (len(currentSubstring) > len(longestSubstring)):     # if the current substring value is greater then longest substring value (will ignore equal length)
            longestSubstring = currentSubstring                 # update  longest substring with now new value
    
    print ("Original String: ", string)
    print("Longest Substring is: ", longestSubstring)
    print("Length of Longest Substring: ", len(longestSubstring))

string = input("Enter String: ")
longestSubstring(string)
