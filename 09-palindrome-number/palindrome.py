class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = ""
        for num in str(x)[::-1]:
            reversed_num += num

        if x == int(reversed_num):
            return True
        else:
            return False

print(Solution().isPalindrome(121)) 