def fact(n):
	assert n>=0 and int(n) == n, "n must be a positive integer"
	if n == 1:
		return n
	else:
		return n * fact(n-1)

print(fact(-1))