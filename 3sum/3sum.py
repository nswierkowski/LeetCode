class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 : return []
        
        i = 1
        dic = {nums[0] : 0}
        previous_elements = set(nums[0])
        res = set()
        for num1 in nums[1:]:
            for num2 in nums[i+1:] :
                num3 = 0 - num2 - num1
                if num3 in dic :
                    new_res1 = [num1,num2,num3]
                    new_res1.sort()
                    res.add(tuple(new_res1))
            dic.update({num1 : i})
            i += 1
        return map(list, res)
