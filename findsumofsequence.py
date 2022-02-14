#Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
#comment 
def findsubarray(length,sum,input):
    j = 0
    current_sum = 0
    while j < length:
        i = j
        while current_sum < sum and i < length:
            current_sum = current_sum + input[i]
            if current_sum == sum:
                print j,i
            i = i +1
        current_sum = 0
        j = j + 1
findsubarray(10,15,[1,2,3,4,5,6,7,8,9,10])
