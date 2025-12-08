class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:


            n=len(nums)
            arr=[]
            for i in range(n):
                count=0
                for j in range (n):
                    if nums[i]>nums[j]:
                        count+=1
                arr.append(count)
            return arr
