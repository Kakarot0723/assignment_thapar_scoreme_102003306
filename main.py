
### 2. `main.py`

"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

from collections import deque

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order


def longest_path(graph):
    n = len(graph)
    
    def dfs(node):
        if memo[node] != -1:
            return memo[node]
        
        max_length = 0
        for neighbor, weight in graph[node]:
            max_length = max(max_length, dfs(neighbor) + weight)
        
        memo[node] = max_length
        return max_length
    
    memo = [-1] * n
    max_path = 0
    
    for node in range(n):
        max_path = max(max_path, dfs(node))
    
    return max_path
# Example usage:
graph = [
    [(1, 3), (2, 2)],
    [(3, 4)],
    [(3, 1)],
    []
]
print(longest_path(graph))  # Output: 7