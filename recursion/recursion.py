import time

def recursion(x, arr=None):
	if arr is None:
		arr = []
	if x > 100:
		return arr
	arr.append(x)
	return recursion(x+1, arr)

start = time.time()
x = recursion(1)
print(x)
end = time.time()
recur = end - start

arr = []
start = time.time()
for x in range(101):
	arr.append(x)
x = arr
print(x)
end = time.time()
itr = end - start

if recur < itr:
	print("Recursion is fast")
else:
	print("Iteration is fast by", (recur-itr)/itr*100)