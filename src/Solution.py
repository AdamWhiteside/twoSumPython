class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair not in dict.keys():
                dict[nums[i]] = i;
            else:
                return [i, dict[pair]]