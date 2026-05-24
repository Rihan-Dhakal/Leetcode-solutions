class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set(nums1)
        res=[]
        for j in nums2:
            if j in seen:
                res.append(j)
                seen.remove(j)
        return res