# Graph Data Structure

A graph is a collection of vertices (nodes) connected by edges. Graphs can be directed or undirected, weighted or unweighted.

## Graph Types

### By Direction
- **Directed Graph (Digraph)**: Edges have direction (A → B)
- **Undirected Graph**: Edges are bidirectional (A ↔ B)

### By Weight
- **Weighted Graph**: Edges have weights/costs
- **Unweighted Graph**: All edges have equal weight (usually 1)

### By Connectivity
- **Connected Graph**: Path exists between any two vertices
- **Disconnected Graph**: Some vertices are unreachable from others

## Graph Representations

### 1. Adjacency List
```python
# Most common representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# For weighted graphs
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 5)],
    'C': [('A', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
```

### 2. Adjacency Matrix
```python
# For dense graphs
# graph[i][j] = weight of edge from i to j
graph = [
    [0, 4, 2, 0],
    [4, 0, 0, 5],
    [2, 0, 0, 1],
    [0, 5, 1, 0]
]
```

### 3. Edge List
```python
# For sparse graphs
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]
```

## Graph Traversal Algorithms

### Depth-First Search (DFS)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)  # Process vertex
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Iterative DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process vertex
            stack.extend(reversed(graph[vertex]))
    
    return visited
```

### Breadth-First Search (BFS)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)  # Process vertex
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited
```

## Common Graph Problems

### 1. Path Finding
```python
def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return True
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True
    
    return False

def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = find_path(graph, neighbor, end, path)
            if new_path:
                return new_path
    
    return None
```

### 2. Cycle Detection
```python
def has_cycle(graph):
    visited = set()
    rec_stack = set()
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False
```

### 3. Connected Components
```python
def connected_components(graph):
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    
    return components
```

### 4. Topological Sort
```python
def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]  # Reverse to get correct order
```

## Shortest Path Algorithms

### 1. Dijkstra's Algorithm (Single Source)
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

### 2. Floyd-Warshall (All Pairs)
```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize distances
    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

## Minimum Spanning Tree

### Kruskal's Algorithm
```python
def kruskal(edges, num_vertices):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    parent = list(range(num_vertices))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    mst = []
    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    
    return mst
```

## Time Complexities

### Traversal
- **DFS**: O(V + E) where V = vertices, E = edges
- **BFS**: O(V + E)

### Shortest Path
- **Dijkstra**: O((V + E) log V) with binary heap
- **Floyd-Warshall**: O(V³)

### MST
- **Kruskal**: O(E log E)
- **Prim**: O((V + E) log V)

## Common Mistakes
1. **Infinite loops**: Always mark vertices as visited
2. **Stack overflow**: Use iterative approach for deep graphs
3. **Wrong data structure**: Choose appropriate representation
4. **Memory issues**: Be careful with large graphs
5. **Direction**: Handle directed vs undirected graphs correctly

## Related Algorithms
- **Tree algorithms**: DFS, BFS on trees
- **Dynamic Programming**: Shortest path problems
- **Greedy algorithms**: MST algorithms
- **Network flow**: Max flow, min cut problems
