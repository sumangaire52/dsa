#789

def sum_of_digits(n:int):
	if n < 10:
		return n
	else:
		return n%10 + sum_of_digits(n//10)

print(sum_of_digits(1001))