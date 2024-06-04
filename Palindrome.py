#Palindrome 


'''Palindrome means to if the string reversed it remains same as it was. '''




'''
Time complexity: O(n)
Auxiliary Space: O(1)

'''



# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "bUlUb"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
