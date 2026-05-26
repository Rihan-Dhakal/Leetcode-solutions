class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for n in nums:
            if n == first or n == second or n == third:
                continue

            if n > first:
                third = second    # second drops to third
                second = first    # first drops to second
                first = n 
            elif n > second:
                third = second    # second drops to third
                second = n    

            elif n > third:
                third = n 
        return third if third != float('-inf') else first

