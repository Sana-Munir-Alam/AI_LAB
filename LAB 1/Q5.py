def stringFunctions(string):                # Function that takes string as a parameter
    vowel = 0
    consonants = 0
    characters = 0
    for ch in string:
        if (ch in 'aeiouAEIOU'):            # check for vowels in string
            vowel += 1                      # if yes increase vowel counter
            characters +=1                  # and increase char counter
        elif (ch.isalpha()):                # check if not vowel are they still alphabet if yes then they are consonants
            consonants +=1
            characters +=1
        else:                               # they are space, comma, speech marks etc
            characters +=1
    
    return {'total_chars': characters, 'vowels': vowel, 'consonants': consonants}

string = input("Enter String: ")
dict = stringFunctions(string)
print ("Original String: ", string)
print ("The dict is: ", dict)
