class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        costs = {K: 0}
        
        for u, v, w in times:
            graph[u].append((w, v))
            
        h = [(0, K)]
        
        while h:
            cost, u = heappop(h)
            
            if u in graph:
                for c, v in graph[u]:
                    next = cost + c
                    if v not in costs or next < costs[v]:
                        costs[v] = next
                        heappush(h, (next, v))
        
        if len(costs) != N:
            return -1
        
        return max(costs.values())
