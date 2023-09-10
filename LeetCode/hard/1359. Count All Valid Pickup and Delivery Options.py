from math import factorial, pow
MOD = 10**9 + 7 

class Solution:
    def countOrders(self, n: int) -> int:
        two_n_fact = factorial(2 * n) % MOD
        two_pow_n = pow(2, n, MOD)
        return (two_n_fact * pow(two_pow_n, -1, MOD)) % MOD