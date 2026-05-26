class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared= [n**2 for n in nums]
        squared.sort()
        return squared