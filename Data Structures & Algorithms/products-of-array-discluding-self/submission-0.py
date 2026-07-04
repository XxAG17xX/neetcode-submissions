class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        for i in range(len(nums)):
           output[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
        return output