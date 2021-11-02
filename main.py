# # Warm-up
# #1 Evaluate 7 - 3 % 4 without coding. 4
# print(7 - 3 % 4)
# #2 Evaluate 8 % 2 / 4 without coding. 0.0
# print(8 % 2 / 4)
# #3 Evaluate 9 - 2 ** 3 without coding. 7
# print(9 - 2 % 3)
# #4 Write a command to output True or False if the first character of “Regis” is “R”.
# print("Regis".startswith("R"))
# #5 Write a command to output True or False if the last character of “Yankees” is “k”.
# print("Yankees".endswith("k"))
# #6 Using code, what is the index position of “R” in “I love Regis”?
# print("I love Regis".find("R"))
# #7 Using code, convert “Mets” to “Jets”
# print("Mets".replace("M", "J"))

# Today's Lesson - String functions 3

#islower() - returns True if all letters are lowercase.

s = "hello"
print(s.islower())  # True 

#isupper() - returns True if all letters are uppercase, else False 
s2 = "HELLO"
print(s2.isupper())  # True 
print(s.isupper())   # False 

# isspace() - returns True if the string contains only whitespace (" ", \n, \t)
s3 = " "
print(s3.isspace())  # True 
print(s.isspace())  # False 

s4 = "hello4$"
print(s4.islower()) # True 

# isalpha() - returns True if string has only letters 
s5 = "hello"
s6 = "hello4"
print(s5.isalpha())  # True
print(s6.isalpha()) # False 

# isdigit() - returns True if string has only digits 
s7 = "1234"
print(s7.isdigit())  # True 
print(s5.isdigit())  # False 
print(s6.isdigit())  # False 
s8 = "1234$"
print(s8.isdigit()) # False 

# isalnum() - returns True if only letters and/or digits 
s9 = "abc$"
print(s9.isalnum()) #False 
s7 = "1234"
print(s7.isalnum())  # True 
s10 = "abc123"
print(s10.isalnum()) # True 
s11 = "abc"
print(s11.isalnum())  # True 

s12 = " \n\t"
print(s12.isspace())  # True 

s13 = "ABabc" 
print(s13.isalpha())  # True 
print(s13.isupper())  # False 





