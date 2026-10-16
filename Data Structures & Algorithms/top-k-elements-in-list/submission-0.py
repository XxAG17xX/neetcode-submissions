class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
            i += 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in seen.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res