def power(n, p):
	if p == 1:
		return n
	return n * power(n, p-1)

print(power(2,5))