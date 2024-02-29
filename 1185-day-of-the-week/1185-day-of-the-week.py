import datetime

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        
        1971.1.1 Fri
        1971.1.2 Sat
        1971.1.3 Sun
        1971.1.4 Mon
        1971.1.5 Tue
        1971.1.6 Wed
        1971.1.7 Thu
        
        """
        
        week = {0 : 'Monday',
                1 : 'Tuesday',
                2 : 'Wednesday',
                3 : 'Thursday',
                4 : 'Friday',
                5 : 'Saturday',
                6 : 'Sunday'}
        
        day = datetime.date(year, month, day)
        return week[day.weekday()]