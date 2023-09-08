class Solution:
    def average(self, salary: list[int]) -> float:
        lmao = salary
        _ = lmao.remove(max(lmao))
        _ = lmao.remove(min(lmao))
        return sum(lmao)/len(lmao)