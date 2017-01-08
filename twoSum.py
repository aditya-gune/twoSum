class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        decoratedNums = []
        b = 0
        for a in nums:
            decoratedNums.append((a, b))
            b += 1
        
        result = []
        for i in decoratedNums:
            for j in decoratedNums:
                if (i[0] + j[0] == target):
                    if (i[1] != j[1]):
                        result.append(i[1])
                        result.append(j[1])
                        return result
