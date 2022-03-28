from sys import argv
c = 0
sum1 = 0
for i in range(10):
	argv[i] = input()
	m = int(argv[i]/2)
	for j in range(2,m):
		if argv[i]%j == 0:
			c = 1
		sum1 += argv[i]
print(sum1)