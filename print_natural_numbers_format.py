import sys
a = 0
result = 0
m = 1
temp = 1
def find_number_of_digits(N):
	a = 1
	while(N):
		if N/10>0:
			N = N/10
			a+=1
		else:
			N =N/10
	return a
	
N = int(sys.argv[1])
n = find_number_of_digits(N)
print("Number of digits in number %s is %s"%(N,n))

for each in range(1,n+1):	
	for i in range(temp,N+1):
		k = m*10
		if i < k+1:
			if not i%k == 0:
				result = (result*k)+i
			else:
				result = (result*k*10)+i
				break
	temp = i+1
	m = 10**each
print(result)