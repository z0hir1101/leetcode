class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = 1 << 0

        for num in nums:
            dp |= dp << num

        return (dp & (1 << sum(nums) // 2)) != 0   


nums = list(map(int, input().split()))
print(Solution.canPartition(None, nums))