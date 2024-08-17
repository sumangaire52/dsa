def convert_to_binary(x):
	if x == 0:
		return 0
	else:
		return x%2 + 10 * (convert_to_binary(x//2))

for x in range(100):
	print(convert_to_binary(x))