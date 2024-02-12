letter = input("Enter a letter: ")

if letter in ["a", "e", "i", "o", "u"]:
    print("This is a vowel.")
elif letter == "y":
    print("This letter is sometimes vowel and sometimes consonant.")
else:
    print("This is a consonant.")
