arr = []
def fibonacci(n):
	if n in [0,1]:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

for x in range(10):
	arr.append(fibonacci(x))
print(arr)