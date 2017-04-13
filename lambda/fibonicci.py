limit = 10
fib = []
fib.append(0)
fib.append(1)
for i in range(limit):
    data1 = fib[i]+fib[i+1]
    fib.append(data1)
print fib

