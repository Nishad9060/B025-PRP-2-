str = input("Enter a word :")
const =[]
vowel =[]
for i in str:
    if i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u':
        vowel.append(i)
    else:
        const.append(i)
print("vowels :",vowel)
print("consonanats :",const)
