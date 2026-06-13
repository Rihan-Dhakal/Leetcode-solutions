class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        sum=0
        if n<0:
        
            return False
        
        while x>0:
        
            ld=x%10
            sum=sum*10 + ld
            x=x//10
            
        return sum==n