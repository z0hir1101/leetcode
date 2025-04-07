class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            comp = target-num
            if comp in hash_map:
                return [i, hash_map[comp]]
            hash_map[num] = i
        return []


nums = list(map(int, input().split()))
target = int(input())
print(*Solution.twoSum(None, nums, target))
