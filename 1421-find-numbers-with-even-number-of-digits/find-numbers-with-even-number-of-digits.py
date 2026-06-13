class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i=0
        for num in nums:
            y=0
            while num>0:
                
                num=num//10
                y+=1
            if y%2==0:
                i+=1
        return i
