from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        uniq = set()
        count = 0
        for f in freq.values():
            while f > 0 and f in uniq:
                f -= 1
                count += 1
            uniq.add(f)
        return count