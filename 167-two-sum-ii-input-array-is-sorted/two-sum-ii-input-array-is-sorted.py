class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map={}
        result= None
        for i in range(len(numbers)):
            if numbers[i] in map:
                result= [map[numbers[i]]+1,i+1]
                print(result)
                return result
            map[target-numbers[i]]=i
        
        return []