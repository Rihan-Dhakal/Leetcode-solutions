class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        sum=0
        while n >0:
           
            ld=n%10
            sum=(sum*10)+ld
            n=n//10
        
        return x==sum