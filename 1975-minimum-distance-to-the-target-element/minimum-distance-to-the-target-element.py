class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        diff=[]
        for i,num in enumerate(nums):
            if num==target:
                j=i
                diff.append(abs(j-start))

        return min(diff)

        