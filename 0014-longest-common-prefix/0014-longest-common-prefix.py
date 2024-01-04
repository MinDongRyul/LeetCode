class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        len_strs = [len(str_) for str_ in strs]
        
        min_len = min(len_strs)

        strs = [str_[:min_len] for str_ in strs]
        for idx in range(min_len, 0, -1):
            temp = [str_[:idx] for str_ in strs]
            if len(set(temp)) == 1:
                return temp[0]
        return ""