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

        # faster answer
        # time = list(time)  # Convert to list for easier manipulation

        # # Handling the first two characters for hours
        # if time[0] == '?':
        #     time[0] = '2' if time[1] in '?0123' else '1'
        # if time[1] == '?':
        #     time[1] = '3' if time[0] == '2' else '9'

        # # Handling the last two characters for minutes
        # if time[3] == '?':
        #     time[3] = '5'
        # if time[4] == '?':
        #     time[4] = '9'

        # return ''.join(time) 