#Here we define a func that defines array and its components 

def findFirstMissing(array, start, end): 

	if (start > end): 
		return end + 1

	if (start != array[start]): 
		return start; 

	mid = int((start + end) / 2) 

	# Left half has all elements 
	# from 0 to mid 
	if (array[mid] == mid): 
		return findFirstMissing(array, 
						mid+1, end) 

	return findFirstMissing(array, 
						start, mid) 


# driver program to test above function 
arr = [0, 1, 2, 3, 4, 5, 6, 7, 10] 
n = len(arr) 
print("Smallest missing element is", 
	findFirstMissing(arr, 0, n-1)) 


