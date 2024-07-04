class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        deck = sorted(deck, reverse=True)
        output = [deck.pop(0)]
        
        while deck:
            output.insert(0, output.pop())
            output.insert(0, deck.pop(0))
                
        return output