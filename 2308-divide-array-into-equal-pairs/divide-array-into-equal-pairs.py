from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2==1:
            return False
        count=Counter(nums)
        for freq in count.values():
            if freq%2==1:
                return False
        return True


        