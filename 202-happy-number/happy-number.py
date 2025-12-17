class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.get_square_sum(n)

            if n == 1:
                return True

        return False

    def get_square_sum(self, n: int) -> int:
        output = 0

        while n > 0:
            digit = n % 10
            output += digit * digit
            n //= 10

        return output