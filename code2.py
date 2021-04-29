
def getMaxOperations(li):
	opr = 0
	i=0
	l = len(li)
	print("length",l)
	for i in range(l-1):
		#print("we have a list that is:", li)
		while li[i] == li[i+1]:
			li[i+1] = li[i+1] * 10 
			print("we have a list that is:", li)
			opr = opr+1
		while li[i]>li[i+1]:
			li[i+1] = li[i+1] * 10 
			print("we have a list that is:", li)
			opr = opr+1
	return opr

def main():
	t = int(input())
	while (t != 0):
		n= int(input())
		li = []
		while (n > 0):
			v = int(input())
			li.append(v)
			n=n-1
		#print(li)
		res = getMaxOperations(li)
		print("res",res)
		t = t-1

main()