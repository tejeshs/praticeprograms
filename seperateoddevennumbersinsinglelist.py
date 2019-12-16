arr=[2,5,4,6,9,7,8,10]

left=0
right=len(arr)-1
while left < right:
   while arr[left] % 2 == 0 and left < right:
      left=left+1
      
   while arr[right] % 2 !=0 and left < right:
      right=right-1
      
   arr[left],arr[right] = arr[right],arr[left] 
   left += 1
   right = right-1
