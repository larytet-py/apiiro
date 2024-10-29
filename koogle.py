from collections import defaultdict
from typing import List, Dict, Tuple

'''
Object Koogler with API Update and Lookup 
Match from the first symbol
'''
class Koogle:
    def __init__(self):
        self.score: Dict[str, int]  = {}
        self.lookup: defaultdict = defaultdict(list)

    '''
    Update tables of scroes and table of lookups
    '''
    def Update(self, pattern: str):
        iterator = SubstringIterator(pattern)
        for  prefix in iterator:
            if prefix not in self.score:
                self.score[prefix] = 0
            if prefix not in self.lookup:
                self.lookup = []

            self.score[prefix] += 1
            self.lookup[prefix].append(prefix)
            

    '''
    Return top matches for the pattern
    '''
    def Suggest(self, pattern: str, size: int):
        iterator = SubstringIterator(pattern)
        allMatchingScores = {}
        for prefix in iterator:
            for s in self.lokup[prefix]:
                allMatchingScores[s] = self.score[s]

        return getTopScores(allMatchingScores)


'''
return up to top "size" scores
'''
def getTopScores(scores: Dict[str, int], size: int) -> List[str, int]:
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    size = min(size, len(sorted_scores))

    return sorted_scores[:size]


class SubstringIterator:
    def __init__(self, s: str):
        self.s = s
        self.curent = 1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.curent > len(self.s):
            raise StopIteration
        res = self.s[:self.curent]
        self.curent += 1

    

