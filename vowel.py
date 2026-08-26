vowel
ch = input("Enter a single character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Invalid Input")
elif ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")