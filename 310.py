from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
       if n <= 2:
           return [i for i in range(n)]

       graph = defaultdict(list)
       num_edges = defaultdict(int)
       remaining_nodes = [i for i in range(n)]

       for edge in edges:
           graph[edge[0]].append(edge[1])
           graph[edge[1]].append(edge[0])
           num_edges[edge[0]] += 1
           num_edges[edge[1]] += 1
       
       leaves = deque()
       new_leaves = deque()

       for i in range(n):
           if num_edges[i] == 1:
               leaves.append(i)

       while True:
            while leaves:
                leaf = leaves.popleft()
                remaining_nodes.remove(leaf)
                for node in graph[leaf]:
                    num_edges[node] -= 1
                    if num_edges[node] == 1:
                        new_leaves.append(node)
            
            if len(remaining_nodes) <= 2:
                return remaining_nodes
            else:
                leaves = new_leaves
                new_leaves = deque()

       return remaining_nodes