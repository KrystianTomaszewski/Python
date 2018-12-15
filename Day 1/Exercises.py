a = "aaaaabbbbcccc"


for letter in a:
    if letter in dictionary:
        dictionary[letter] +=1
    else:
        dictionary[letter] = 1
print (dictionary)