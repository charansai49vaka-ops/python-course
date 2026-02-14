# String method function is used to change the alphabets in the string as we want by totally coberted into capitals or small has we want
#there is somany number of built-in function
# upper():Converts all characters in the string to uppercase.
# lower():Converts all characters to lowercase.
# capitalize(): Converts the first character of the string to uppercase and the rest to lowercase
# title(): Converts the first character of each word to uppercase.
# strip(): Removes leading and trailing characters, defaulting to whitespace.
# lstrip(): Removes only leading characters.
# rstrip(): Removes only trailing characters.
# replace(): Replaces occurrences of a substring.means we can able to change the swap a word in a string function
# split(): Splits the string into a list based on a separator.(",")
# isalnum(): Checks for alphanumeric characters.
# isalpha(): Checks for alphabetic characters.
# isdigit(): Checks for digits.
# islower(): Checks for lowercase characters.
# isupper(): Checks for uppercase characters.
# isspace(): Checks for whitespace characters.
# istitle(): Checks if the string is title-cased.
# isidentifier(): Checks if the string is a valid Python identifier. 

name="sai charan"
print(name.upper())
print(name.lower())
print(name.capitalize()) #starting letter capital
print(name.title())
print(name.rstrip()) #remove the space in right side
print(name.lstrip()) #remove the space in left side
print(name.strip()) #remove the space in both right and left
print(name.replace("charan","Virat Kholi"))#replace the woeds in the string as we want
print(name.split(" "))
s=name.split()
print(s)

cha="sai,charan,vaka,naidu,vk"
sc=cha.split(",")
print(sc) 
print(name.isalnum())
print(name.isdigit())
print(name.isalpha())


name="  adi lakshmi  "
print(name.upper())
print(name.lower())
print(name.capitalize())

print(name.title())
print(name.rstrip())
print(name.lstrip())
print(name.strip())
print(name.replace("adi", "aadi"))
print(name.join(","))