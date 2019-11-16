#replace a word from the string and convert the string into uppercase.
#Hint : use function but yo need to find which one

string=str(input("Enter any string you like: "))
word=str(input("Which one would you like to replace?? \n "))
word2=str(input("what would you like to replace to?? \n "))
new=(string.replace(word,word2)) #replacing the string
print(new)
print(new.upper())