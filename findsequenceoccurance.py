arr = "abcxyabcdefghdsafeabcdabc"
start = 0
pointer = start + 1
length = len(arr)
test = {}
temp = 98
while start < pointer and pointer < length:
    while pointer < length and chr(temp) == arr[pointer]:
        temp = temp + 1
        pointer = pointer + 1
    key = arr[start: pointer]
    if len(key) > 1:
    	if test.__contains__(key):
        	test[key] = test[key] + 1
    	else:
        	test[key] = 1
    start = pointer
    pointer = pointer + 1
    temp = 98
print(test)
