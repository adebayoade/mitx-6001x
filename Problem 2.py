# Problem 2
# Write a program that prints the number of times the string 'bob' occurs in s
# By Adebayo Ade 10/5/2019
# s = 'azcbobobegghakl' uncomment this line to run code in IDE

s = 'azcbobobegghakl'

startIdx = 0
stepIdx = 3
bobCount = 0

for i in range(len(s)):
    if s[startIdx:stepIdx] == 'bob':
        bobCount += 1
    startIdx += 1
    stepIdx += 1

print('Number of times bob occurs is: ' + str(bobCount))
