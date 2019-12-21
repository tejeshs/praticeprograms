#Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

def findsum(sum,array1,array2):
	if len(array1) != len(array2):
		return -1
	length = len(array1)
	i = 0
	current_sum = 0
	while i < length:
		j = 0
		while j < length:
			current_sum = array1[i] + array2[j]
			if current_sum == sum:
				print array1[i],array2[j]
			j = j + 1
		i = i + 1
findsum(9,[1,2,4,5,7],[5,6,3,4,8])
