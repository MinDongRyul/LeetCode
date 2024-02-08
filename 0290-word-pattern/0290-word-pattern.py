class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        temp_pa, temp_pa_lst = {}, []
        temp_s, temp_s_lst = {}, []
        
        for idx, val in enumerate(pattern):
            if val not in temp_pa.keys():
                temp_pa[val] = idx
                temp_pa_lst.append(idx)
            else:
                temp_pa_lst.append(temp_pa[val])
            
        for idx, val in enumerate(s.split()):
            if val not in temp_s.keys():
                temp_s[val] = idx
                temp_s_lst.append(idx)
            else:
                temp_s_lst.append(temp_s[val])
            
        if temp_pa_lst == temp_s_lst:
            return True