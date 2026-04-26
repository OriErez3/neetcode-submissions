class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_res = 0
        for num in nums:
            xor_res ^= num
        return xor_res