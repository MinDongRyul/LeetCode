class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        r = []
        number = number.replace('-','').replace(' ','')
        while len(number) > 4:
            r.append(number[:3])
            number = number[3:]
            
        if len(number) == 4:
            r.append(number[:2])
            r.append(number[2:])
        else:
            r.append(number)
            
        return '-'.join(r)