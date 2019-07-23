def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        currentMax = nums[0]
        maxSoFar = nums[0]
        
        for i in range(1,len(nums)):
            currentMax = max(nums[i], nums[i] + currentMax)
            maxSoFar = max(currentMax, maxSoFar)
        
        return maxSoFar