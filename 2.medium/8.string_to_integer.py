class Solution:
    def myAtoi(self, s: str) -> int:
        cur = res = 0
        sign = 1

        while cur < len(s) and s[cur].isspace():
            cur += 1
        if cur == len(s):
            return 0
        if s[cur] == '-' or s[cur] == '+':
            sign = -1 if s[cur] == '-' else 1
            cur += 1

        while cur < len(s) and s[cur].isdigit():
            res = res * 10 + int(s[cur])
            cur += 1
        if (res * sign < -2147483648):
            return -2147483648
        if (res * sign > 2147483647):
            return 2147483647
        return res * sign


s = input()
print(Solution.myAtoi(None, s))
