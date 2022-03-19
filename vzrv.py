n = int(input()) + 3
y = [0]*n
y[1] = 1
y[2] = 1
for i in range (3, n):
	y[i] = y[i-1] + y[i-2] + y[i-3]

print(y[n-1])