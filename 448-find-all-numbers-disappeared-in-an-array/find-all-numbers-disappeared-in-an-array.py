class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        

        newnum=set(nums)
        retur=[]

        for i in range(1,len(nums)+1):
            if i  not in newnum:
                retur.append(i)
        return retur 