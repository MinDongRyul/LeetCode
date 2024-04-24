from collections import Counter
import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # cs = sorted(Counter(s).items(), key=lambda x : x[1], reverse=True)
        # solution 1
        # r = ''
        # for val in cs:
        #     r += val[0] * val[1]
        
        # solution 2
        # r = ''.join([val[0] * val[1] for val in cs])
        # return r

        # solutuon 3
        # Use Counter to get the frequency of each character
        char_freq = Counter(s)
        # Use max heap to sort characters based on frequency
        max_heap = [(-freq, char) for char, freq in char_freq.items()]
        heapq.heapify(max_heap)
        # Build the result string
        result = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result += char * (-freq)
        return result
        
        