class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adj = {i:[] for i in range(n)}
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj[node]:
                dfs(neighbour)
        
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count
                