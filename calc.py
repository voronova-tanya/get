n = int(input())
x = [0]*n
for i in range (1, n+1):
    x[i-1] = list([i, 0])

for i in range (n):
    if i+1 < n and (x[i][1] + 1 < x[i+1][1] or x[i+1][1] == 0) :
        x[i+1][1] = x[i][1] + 1
    if (i+1)*2-1 < n and (x[i][1] + 1 < x[(i+1)*2-1][1] or x[(i+1)*2-1][1] == 0) :
        x[(i+1)*2-1][1] = x[i][1] + 1
    if (i+1)*3-1 < n and (x[i][1] + 1 < x[(i+1)*3-1][1] or x[(i+1)*3-1][1] == 0) :
        x[(i+1)*3-1][1] = x[i][1] + 1

print(x[n-1][1])