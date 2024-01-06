class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_ ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }

        temp = [dict_[s[0]]]

        for sym in s[1:]:
            if temp[-1] >= dict_[sym]: # 1000 >= 100 , 10 >= 10
                temp.append(dict_[sym])
            else: # 100 < 1000, 1 < 5
                temp_num = temp.pop()
                temp.append(dict_[sym] - temp_num)

        total = sum(temp)

        return total