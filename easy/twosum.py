class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i, entry in enumerate(nums):
            t = target - entry
            if t in hash_dict:
                return [hash_dict[t], i]
            hash_dict[entry] = i
        return []
        
