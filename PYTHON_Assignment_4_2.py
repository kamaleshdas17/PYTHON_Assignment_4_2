## Problem Statement1
## Write a Python program using function concept that maps list of words into a list of integers
## representing the lengths of the corresponding words.

def wordToLength(l):
	output=[len(word) for word in l]
	
	return output
	

lst=['Python','Array','List','Dictionary','abcde','Set']

print ('Given list is {} And the lenght of each element in the list is: {}'.format(lst, wordToLength(lst)))

print ('------------------------------')
print ('------------------------------')

## Problem​ ​Statement​ ​2:
## Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
## a vowel, False otherwise.


import sys
def checkVowel(c):
	vowel_set='AEIOU'
	
	if vowel_set.find(c.upper()) >=0:
		return 'True'
	else:
		return 'False'
try:
	while(1):
		c=input('Please enter any character from [a-z] or [A-Z]. Will be True if Vowel else False. To exit, type (exit) : ')
		if c=='exit':
			sys.exit(0)
		else:
			print (checkVowel(c))
except KeyboardInterrupt:
	print('interrupted!!')
	