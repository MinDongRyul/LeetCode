class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prep_s = ''
        for val in s:
            if val.isalpha():
                prep_s += val.lower()
            elif val.isdigit():
                prep_s += val
        
        for i in range(len(prep_s)//2):
            if prep_s[i] != prep_s[::-1][i]:
                return False
        return True