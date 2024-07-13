class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1, version2 = version1.split('.'), version2.split('.')
        len_version1, len_version2 = len(version1), len(version2)

        if len_version1 > len_version2:
            version2 = version2 + ['0'] * abs(len_version1 - len_version2)
        else:
            version1 = version1 + ['0'] * abs(len_version1 - len_version2)
            
        for idx in range(len(version1)):
            num1, num2 = int(version1[idx]), int(version2[idx])  
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0