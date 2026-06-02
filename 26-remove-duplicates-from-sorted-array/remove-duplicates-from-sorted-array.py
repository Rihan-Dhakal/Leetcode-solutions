class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                nums[j],nums[i+1]=nums[i+1],nums[j]
                i+=1
        return i+1
        
        