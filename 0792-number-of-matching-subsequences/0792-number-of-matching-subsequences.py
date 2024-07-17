from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        count = 0
        
        # 각 첫번째 알파벳의 단어들로 사전을 만듬
        # words = ['a', 'b', 'ab', 'bca']
        # word_dict[a] = ['a', 'ab']
        # word_dict[b] = ['b', 'bca']
        for word in words:
            word_dict[word[0]].append(word)            
        
        # input S로 부터 알파벳 한개씩 순차로 진행
        for char in S:
            # char : a
            # words_expecting_char = word_dict[a]
            # word_dict[a] = [] 
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            # words_expecting_char = ['a', 'ab']
            for word in words_expecting_char:
                if len(word) == 1: # 만약 길이가 1이면 일치 'a'
                    # Finished subsequence! 
                    count += 1
                else: # 길이가 1이 아니면 그 뒤에 해당하는 알파벳을 key로 남은 알파벳을 value로 저장  
                    word_dict[word[1]].append(word[1:])
        
        # 최종 count return
        return count