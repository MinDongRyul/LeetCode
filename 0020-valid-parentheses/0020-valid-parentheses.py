class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        dict_ = {')': '(', ']':'[', '}':'{'}
        for s_ in s:
            if s_ in ['(', '[', '{']:
                queue.append(s_)
            elif s_ in [')', ']', '}']:
                if not queue:
                    return False
                if queue[-1] == dict_[s_]:
                    queue.pop(-1)
                else:
                    queue.append(s_)
                
        if queue:
            return False
        else:
            return True