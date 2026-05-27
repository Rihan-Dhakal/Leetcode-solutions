class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
            seen1=set(nums1)
            seen2=set(nums2)
            res1=[]
            res2=[]
            for i in seen1:
                if i not in seen2:
                    res1.append(i)
            for i in seen2:
                if i not in seen1:
                    res2.append(i)
            return [res1,res2]
            
