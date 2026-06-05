class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i=0
        
        for num in nums:
            count=0
            
            while num>0:
                
                count=count+1
                num=num//10
            
            if (count%2==0):
                
                i=i+1
        return i
