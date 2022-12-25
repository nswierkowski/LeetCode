class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        dic = {}
        for elem in nums :
            if (target - elem) in dic :
                return [dic[(target - elem)], i]
            else :
                dic.update({elem : i})
            i += 1
        return [i,i]
