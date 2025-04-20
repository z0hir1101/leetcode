class Solution:
    def maxArea(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        mx = (r - l) * min(arr[r], arr[l])

        while r - l > 1:
            if arr[l] > arr[r]:
                tmp = arr[r]
                while r > l and arr[r] <= tmp: r -= 1
            else:
                tmp = arr[l]
                while l < r and arr[l] <= tmp: l += 1

            if (r - l) * min(arr[r], arr[l]) > mx:
                mx = (r - l) * min(arr[r], arr[l])
                
        return mx
                
            
arr = list(map(int, input().split()))
print(Solution.maxArea(None, arr))