class Solution:
    def minElement(self, nums: List[int]) -> int:
            min=float('inf')
            for i in nums:
                sum=0
                while i>0:
                    lastdigit=i%10
                    sum=sum+lastdigit
                    i=i//10
                if min>sum:
                    min=sum
            return min
                
           
