class Solution(object):
    def fib(self, N):
        cache = {}

        def find_fib(n):
            if n in cache:
                return cache[n]
            if n <= 1:
                return n
            return find_fib(n-1) + find_fib(n-2)

        return find_fib(N)
