class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lP, rP = 0, len(numbers)-1
        while True:
            if numbers[lP] + numbers[rP] == target:
                return [lP+1, rP+1]
            elif numbers[lP] + numbers[rP] > target:
                rP = rP - 1 
            else:
                lP = lP + 1
        