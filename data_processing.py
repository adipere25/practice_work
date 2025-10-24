# 1. Convert sentence to uppercase
sentence = input("Please enter a sentence: ")
print(sentence.upper())
print("")  # just a blank line for readability

# 2. Count words in a paragraph
paragraph = input("Please enter a paragraph: ")
words = paragraph.split()
print(f"The paragraph has {len(words)} words.")
print("")

# 3. Check if all characters are digits
string1 = input("Please enter a string: ")
print(string1.isdigit()) 
print("")

# 4. Replace "a" with "o"
string2 = input("Please enter another string: ")
new_string = string2.replace("a", "o")
print(new_string)
print("")

# 5. Print initials from full name
full_name = input("Please enter your full name: ")
name_parts = full_name.split()
initials = ''.join([name[0].upper() for name in name_parts])
print(f"Your initials are: {initials}")
print("")

# 6. Print the length of a string
string3 = input("Please enter one more string: ")
print(f"The length of your string is: {len(string3)}")



#7

