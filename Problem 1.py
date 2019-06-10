# Problem 1
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# By Adebayo Ade 10/5/2019
# s = 'azcbobobegghakl' uncomment this line to run code in IDE
s = 'azcbobobegghakl'
numOfVowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numOfVowels += 1
print('Number of vowels: ' + str(numOfVowels))
