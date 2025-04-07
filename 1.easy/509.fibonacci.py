class Solution:
    def fib(self, n: int):
        n1 = 1
        n2 = 1
        while n > 2:
            n -= 1
            n2 += n1
            n1 = n2 - n1
        return 0 if (n == 0) else n2

n = int(input())
print(Solution.fib(None, n))