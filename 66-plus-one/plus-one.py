class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result= "".join(map(str,digits))
        result=int(result)
        final=result + 1

        again= [int(x) for x in str(final)]
        return again