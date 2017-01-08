def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in nums:
            for j in nums:
                
                if i + j == target and nums.index(i) != nums.index(j):
                    print i, "+", j, "=", i+j
                    result.extend((nums.index(i), nums.index(j)))
                    print result


twoSum([0,4,3,0], 0)
