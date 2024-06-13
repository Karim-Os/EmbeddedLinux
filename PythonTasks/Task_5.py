# Task 5: Write a Python program to test whether a passed letter is a vowel or not.

vowels = "aAeEiIoOuU"

def IsVowel(c):
    if (c in vowels):
        return True
    else:
        return False

A = "a"
print (f"{IsVowel(A)}")
