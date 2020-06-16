

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        distances, seen = {}, {}
        for u, v, cost in flights:
            distances[u] = distances.get(u, []) + [(v, cost)]

        queue = [(src, -1, 0)]
        while queue:
            pos, step, cost = queue.pop(0)
            if pos == dst or step == K:
                continue
            for neighbour, p in distances.get(pos, []):
                if cost + p >= seen.get(neighbour, float('inf')):
                    continue
                seen[neighbour] = cost+p
                queue.append((neighbour, step+1, cost+p))
        return seen[dst] if seen[dst] != float('inf') else -1