class Solution:
    def findMedianSortedArrays(self, l1: list[int], l2: list[int]) -> float:
        for num in l2:
            l1.append(num)
        l1.sort()
        ln = len(l1)

        if ln % 2 == 1:
            return l1[ln // 2]
        else:
            return (l1[ln // 2] + l1[ln // 2 - 1]) / 2


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(Solution.findMedianSortedArrays(None, l1, l2))