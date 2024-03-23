import re

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        word_num = len(text.split())
        space_num = len(re.findall(r'\s', text))
        
        r = ''
        
        if word_num - 1 > 0:
            avg_space = space_num // (word_num - 1)
        
            for text_ in text.split():
                r += text_ + ' ' * avg_space
    
            if len(r) > len(text): return r[:-(len(r) - len(text))]
            elif len(r) < len(text): return r + ' ' * (len(text) - len(r))
            else: return r
        else:
            return text.split()[0] + ' ' * space_num