import re

class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = time.replace('?','.')
        p = re.compile(time)
        for h in range(23, -1, -1):
            h = str(h).zfill(2)
            for m in range(59, -1, -1):
                m = str(m).zfill(2)
                latest_time = h + ':' + m
                if p.match(latest_time):
                    return latest_time