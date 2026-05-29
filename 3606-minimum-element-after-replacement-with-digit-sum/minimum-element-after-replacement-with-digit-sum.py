class Solution:
    def minElement(self, nums: List[int]) -> int:
      
       
            min=float('inf')
            for num in nums:
                sum=0
                while num>0:
                    lastdigit=num%10
                    sum=sum +lastdigit
                    num=num//10
                if min>sum:
                    min=sum
            return min
            
           
