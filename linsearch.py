arr = [1,2,3,5,0,4]
x = int(input())
def searchv(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return True
	return False

b=searchv(arr,x)
if b == True:
	print("Yes")
else:
	print("NO")