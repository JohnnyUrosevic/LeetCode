class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            edge = edges[i]
            graph[edge[0]].append((succProb[i], edge[1]))
            graph[edge[1]].append((succProb[i], edge[0]))
        
        seen = set()
        heap = [(-1.0, start)]
        
        while heap:
            prob, node = heappop(heap)
            seen.add(node)
            
            if node == end:
                return -prob
            
            for (edge_prob, destination) in graph[node]:
                if destination in seen:
                    continue
                
                heappush(heap, (edge_prob * prob, destination))
        
        return 0.0
