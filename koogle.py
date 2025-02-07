from typing import List, Dict, Set, Tuple

'''
Object Koogle with API Search and Suggest
Match from the first symbol
'''
class Koogle:
    def __init__(self):
        self.score: Dict[str, int]  = {}
        self.lookup: Dict[str, Set[str]]  = {}

    '''
    Update tables of scroes and table of lookups
    The function is being calle for all sub strings
    "b", "bo", "boo", "book", ...
    '''
    def suggest(self, pattern: str):
        if pattern not in self.score:
            # {"boo": 0}
            self.score[pattern] = 0


        # {"boo": 1}
        self.score[pattern] += 1            

        iterator = SubstringIterator(pattern)
        for prefix in iterator:
            if prefix not in self.lookup:
                self.lookup[prefix] = set()

            # b, bo, boo, book, ...
            self.lookup[prefix].add(pattern)


    '''
    Return top matches for the pattern
    '''
    def search(self, pattern: str, count: int = 10) -> Dict[str, int]:
        allMatchingScores = {}
        for s in self.lookup[pattern]:
            # b, bo, boo, book, ...
            if len(s) < len(pattern):
                # if given "boo" should I ignore "b", "bo"?
                continue

            # if given "boo" consider "boo", "book", "boom", ...
            allMatchingScores[s] = self.score[s]

        return get_top_scores(allMatchingScores, count)


'''
return up to top "size" scores
'''
def get_top_scores(scores: Dict[str, int], count: int) -> List[Tuple[str, int]]:
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    count = min(count, len(sorted_scores))
    return sorted_scores[:count]

class SubstringIterator:
    def __init__(self, s: str, min_len: int = 1):
        self.s = s
        self.current = min_len

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current > len(self.s):
            raise StopIteration
        res = self.s[:self.current]
        self.current += 1
        return res