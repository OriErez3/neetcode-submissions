class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;
        for (int i = 0; i < nums.size(); i++){
            if (seen.find(nums[i]) == seen.end()) {
                seen[nums[i]] = i;
            }
        for (int i = 0; i<nums.size(); i++){
            int compliment = target - nums[i];
            if (seen.find(compliment) != seen.end() && seen[compliment] != i) {
                return {seen[compliment],i};
            }
        }
        }
    }
};
