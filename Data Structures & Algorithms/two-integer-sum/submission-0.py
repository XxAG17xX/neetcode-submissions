class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        seen=dict()
        while i < len(nums):
            difference = target-nums[i]
            if difference in seen:
                return [seen[difference],i]
            seen[nums[i]]=i
            i+=1


