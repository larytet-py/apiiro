'''
Object Koogler with API Update and Lookup 
Match from the first symbol
'''
class Koogle:
    def __init__(self):
        self.score = {}
        self.lookup = {}

    '''
    Update tables of scroes and table of lookups
    '''
    def Update(self, pattern):
        iterator = SubstringIterator(pattern)
        for  prefix in iterator:
            if prefix not in self.score:
                self.score[prefix] = 0
                self.lokup = []

            self.score[prefix] += 1
            self.lookup[prefix].append(prefix)
            

    '''
    Return top matches for the pattern
    '''
    def Suggest(self, pattern, size):
        iterator = SubstringIterator(pattern)
        allMatchingScores = {}
        for prefix in iterator:
            for s in self.lokup[prefix]:
                allMatchingScores[s] = self.score[s]

        return getTopScores(allMatchingScores)



def getTopScores(scores, size):
    sortes_scores = sorted(scores.items()), key=lambda x: x[1], reverse = True
    size = min(size, len(sortes_scores))
    return sortes_scores[:size]


class SubstringIterator:
    def __init__(self, s):
        self.s = s
        self.curent = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curent > len(self.s):
            raise StopIteration
        res = self.s[:self.curent]
        self.curent += 1

    

