def fib(n: int):
	n1 = 1
	n2 = 1
	while n > 2:
		n -= 1
		n2 += n1
		n1 = n2 - n1
	return n2

a = int(input())
print(fib(a))