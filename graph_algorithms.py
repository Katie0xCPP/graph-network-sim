from collections import deque
import heapq
import random
from typing import Dict, List, Tuple, Any, Set


class Graph:
    def __init__(self, directed: bool = True):
        self.directed = directed
        self.adj: Dict[Any, List[Tuple[Any, float]]] = {}

    def add_edge(self, u, v, weight: float = 1.0):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def neighbors(self, u):
        return [v for v, _ in self.adj.get(u, [])]

    def bfs(self, start):
        visited: Set[Any] = set()
        order: List[Any] = []

        if start not in self.adj:
            return order

        q = deque([start])
        visited.add(start)

        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return order

    def dfs(self, start):
        visited: Set[Any] = set()
        order: List[Any] = []

        if start not in self.adj:
            return order

        stack = [start]

        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)

            for v, _ in reversed(self.adj[u]):
                if v not in visited:
                    stack.append(v)

        return order

    def shortest_path_unweighted(self, start):
        dist: Dict[Any, int] = {}

        if start not in self.adj:
            return dist

        q = deque([start])
        dist[start] = 0

        while q:
            u = q.popleft()
            for v, _ in self.adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    q.append(v)

        return dist

    def dijkstra(self, start):
        dist: Dict[Any, float] = {node: float("inf") for node in self.adj}
        prev = {}
        dist[start] = 0.0

        heap = [(0.0, start)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue

            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(heap, (nd, v))

        return dist, prev

    def pagerank_random_walk(self, steps: int = 10000, damping: float = 0.15):
        nodes = list(self.adj.keys())
        if not nodes:
            return {}

        current = random.choice(nodes)
        counts = {node: 0 for node in nodes}

        for _ in range(steps):
            counts[current] += 1

            if random.random() < damping or not self.adj[current]:
                current = random.choice(nodes)
            else:
                neighbors = [v for v, _ in self.adj[current]]
                current = random.choice(neighbors)

        total = sum(counts.values())
        return {node: count / total for node, count in counts.items()}


def generate_random_graph(n: int, p: float, directed: bool = False) -> Graph:
    g = Graph(directed=directed)

    for i in range(n):
        g.adj.setdefault(i, [])

    for i in range(n):
        for j in range(i + 1, n) if not directed else range(n):
            if i != j and random.random() < p:
                g.add_edge(i, j)

    return g
