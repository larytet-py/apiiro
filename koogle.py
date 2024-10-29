from collections import defaultdict
from typing import List, Dict, Tuple

'''
Object Koogle with API Search and Suggest
Match from the first symbol
'''
class Koogle:
    def __init__(self):
        self.score: Dict[str, int]  = {}

    '''
    Update tables of scroes and table of lookups
    The function is being calle for all sub strings
    "b", "bo", "boo", "book", ...
    '''
    def Suggest(self, pattern: str):
        if pattern not in self.score:
            # {"boo": 0}
            self.score[pattern] = 0
        # {"boo": 1}
        self.score[pattern] += 1            
           

    '''
    Return top matches for the pattern
    '''
    def Search(self, pattern: str, size: int) -> Dict[str, int]:
        iterator = SubstringIterator(pattern)
        allMatchingScores = {}
        for prefix in iterator:
            # b, bo, boo, book, ...
            for s in self.score[prefix]:
                if len(prefix) < len(pattern):
                    # if given "boo" should I ignore "b", "bo"?
                    continue

                # if given "boo" consider "boo", "book", "boom", ...
                allMatchingScores[s] = self.score[s]

        return get_top_scores(allMatchingScores)


'''
return up to top "size" scores
'''
def get_top_scores(scores: Dict[str, int], size: int = 10) -> List[str, int]:
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    size = min(size, len(sorted_scores))

    return sorted_scores[:size]


class SubstringIterator:
    def __init__(self, s: str, min_len: int = 1):
        self.s = s
        self.curent = min_len

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.curent > len(self.s):
            raise StopIteration
        res = self.s[:self.curent]
        self.curent += 1

    

