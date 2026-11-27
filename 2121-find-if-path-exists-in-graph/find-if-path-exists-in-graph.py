from collections import defaultdict, deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        stack = deque()
        seen = set()

        stack.append(source)
        seen.add(source) # Only path matters not finding all possible paths
        while stack:
            node = stack.pop()
            if destination in graph[node]:
                return True
            for x in graph[node]:
                if x not in seen:
                    stack.append(x)
                    seen.add(x)
        return False

