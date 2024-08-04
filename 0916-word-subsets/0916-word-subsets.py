class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        # include_dict = defaultdict(int)
        
        # for word2 in words2:
        #     temp = Counter(word2)
        #     for word in temp:
        #         include_dict[word] += temp[word] 
        
        # rm_idx = []
        # for word1 in words1:
        #     temp = Counter(word1)
        #     for word in include_dict:
        #         if include_dict[word] > temp[word]:
        #             rm_idx.append(words1.index(word1))
                    
        # rm_idx = sorted(set(rm_idx), reverse=True)
        # for idx in rm_idx:
        #     words1.pop(idx)
            
        # return words1

        count = collections.Counter()
        for b in words2:
            # "lo" -> count = {"l":1, "o":1}
            # count l= Counter("co") -> count = {"l":1, "o":1, "e":1}, not {"l":1, "o":2, "e":1} 
            count |= collections.Counter(b)
        # not count - Counter(a) : count에서 Counter(a)를 빼고 남는게 없어야 count를 전부 포함하는 word라는 의미
        return [a for a in words1 if not count - Counter(a)]