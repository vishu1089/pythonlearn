# cost=[10,15,20]
# c_len=len(cost)
# cost.append(0)
# dp=[10 for _ in range(c_len+1)]
# print (dp)
# dp[0]=cost[0]
# dp[1]=cost[1]
# for i in range(2,len(dp)):
# 	dp[i] =  min(dp[i-1],dp[i-2]) + cost[i]
# 	print(dp)
# print("\n",dp[-1])



def divisor(n):
	if(n%2 == 0): return True
	else: return False

b=divisor(10)
print(b)