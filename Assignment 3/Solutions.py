"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string="Programming"
reversed_string=string[::-1]
print("Reversed string:",reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name=input("Enter your full name:")
initials="..join([name[0].upper()for name in
full_name.split()])+",
print("initials:",initials)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(string):
  string=string.replace(" ","").lower()
  return string==string[::-1]
user_input=input("Enter a string:")
if is_palindrome(user_input):
  print("It's a palindrome!")
else:
  print("it's not a palindrome")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input("Enter a sentence:")
#split the sentence into words
words=sentence.split()
#count the number of words
word.count=len(words)
#display the result
print("Number of words in the sentence:",word_count)



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
#Original stirng
text="this is a string and it is an example."
#replace "is" with"was"
modified_text=text.replace("is","was")
#print the modified string
print("modified sting:",modified_text)
