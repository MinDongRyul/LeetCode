class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prep_s = ''
        s = s.lower()
        for val in s:
            if val.isalnum():
                prep_s += val
        
        if prep_s[:len(prep_s)//2] != prep_s[::-1][:len(prep_s)//2]:
            return False
        return True