class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            
            graph[a][b] = values[i]
            graph[b][a] = 1.0 / values[i]
        
        result = []
        for query in queries:
            a = query[0]
            b = query[1]
            
            if a not in graph or b not in graph:
                result.append(-1.0)
                continue
            
            seen = set()
            stack = [(a, 1.0)]
            value_added = False
            while stack:
                node, val = stack.pop()
                seen.add(node)
                
                if node == b:
                    result.append(val)
                    graph[a][b] = val
                    value_added = True
                    break
                
                for dest in graph[node].keys():
                    if dest not in seen:
                        stack.append((dest, graph[node][dest] * val))
            
            if not value_added:
                result.append(-1.0)
        
        return result
            
        
