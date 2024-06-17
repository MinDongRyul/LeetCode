from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # fix my answer 
        word_dict = Counter(words)
        temp = 0
        aa = 0
        abba = 0

        for word in word_dict.keys():
            if word[0] == word[-1]:
                aa += word_dict[word] // 2 * 2
                if word_dict[word] % 2 == 1 : temp = 2
            else:
                abba += (min(word_dict[word], word_dict[word[::-1]])) * 0.5
        
        return aa * 2 + int(abba) * 4 + temp

        # my answer
        # word_dict = Counter(words)
        # temp = 0
        # r = 0
        
        # for word in word_dict.keys():
        #     if word[0] == word[-1]:
        #         r += word_dict[word] // 2 * 4
        #         temp = word_dict[word] % 2 * 2
        #     else:
        #         r += (min(word_dict[word], word_dict[word[::-1]])) * 2
        
        # return r + temp