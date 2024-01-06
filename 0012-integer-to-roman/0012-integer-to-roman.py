class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_sym = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }

        total_str = ''
        dict_sym = sorted(dict_sym.items(), key=lambda x: x[1], reverse=True)

        for key, val in dict_sym:
            if num >= val:
                m_cot = num // val
                num %= val
                total_str += key * m_cot

        total_str = total_str.replace('DCCCC','CM').replace('CCCC','CD')
        total_str = total_str.replace('LXXXX','XC').replace('XXXX','XL')
        total_str = total_str.replace('VIIII','IX').replace('IIII','IV')

        return total_str