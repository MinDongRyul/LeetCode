from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        
        cnt = Counter(changed)
        changed = sorted(changed)
        temp = []
        temp2 = []
        
        for key in changed:
            if cnt[key] == 0:continue
            
            y = key * 2
            
            if y in changed:
                temp.append(key)
                cnt[y] -= 1
                cnt[key] -= 1
            else:
                return []

            if cnt[y] < 0 :
                return []
            
        return temp

        # time limit 
        # cnt = Counter(changed)
        # changed = sorted(changed)
        # temp = []
        # temp2 = []
        
        # for val in changed:
        #     if cnt[val] == 0:continue
        #     if cnt[val] < 0: return []
                
        #     y = val * 2
                
        #     if y in changed:
        #         temp.append(val)
        #         temp2.append(y)
        #         cnt[y] -= 1
        #         cnt[val] -= 1
                        
        # if sorted(temp + temp2) == changed:
        #     return temp
        # else:
        #     return []
