class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}        
        for i in xrange(len(nums)):
            tmp = table.get(target - nums[i])
            if tmp != None:
                return [tmp, i+1]
            table[nums[i]] = i+1

