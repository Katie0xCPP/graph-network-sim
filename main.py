from graph_algorithms import Graph, generate_random_graph
from simulation import simulate_propagation


def demo_algorithms():
    print("=== Graph Algorithms Demo ===")

    # Build a small weighted undirected graph
    g = Graph(directed=False)
    edges = [
        ("A", "B", 1),
        ("A", "C", 2),
        ("B", "D", 1),
        ("C", "D", 3),
        ("C", "E", 1),
        ("D", "F", 2),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    # BFS and DFS
    print("\nBFS from A:", g.bfs("A"))
    print("DFS from A:", g.dfs("A"))

    # Shortest paths (unweighted)
    dist_unweighted = g.shortest_path_unweighted("A")
    print("\nUnweighted shortest-path distances from A:")
    for node, d in dist_unweighted.items():
        print(f"  A -> {node}: {d} edges")

    # Dijkstra (weighted shortest paths)
    dist_weighted, prev = g.dijkstra("A")
    print("\nWeighted shortest-path distances from A (Dijkstra):")
    for node, d in dist_weighted.items():
        print(f"  A -> {node}: distance {d}")

    # PageRank-style random walk
    pr = g.pagerank_random_walk(steps=20000, damping=0.15)
    print("\nApproximate PageRank (random walk with teleportation):")
    for node, score in sorted(pr.items(), key=lambda x: x[1], reverse=True):
        print(f"  {node}: {score:.4f}")


def demo_simulation():
    print("\n=== Propagation Simulation Demo ===")

    # Two random graphs with different connectivity
    n_nodes = 20
    sparse_p = 0.05   # low connectivity
    dense_p = 0.2     # higher connectivity

    g_sparse = generate_random_graph(n_nodes, sparse_p, directed=False)
    g_dense = generate_random_graph(n_nodes, dense_p, directed=False)

    initial_seed = [0]  # start spreading from node 0
    p_spread = 0.3      # probability of spreading along each edge
    steps = 10

    history_sparse = simulate_propagation(g_sparse, initial_seed, p_spread, steps)
    history_dense = simulate_propagation(g_dense, initial_seed, p_spread, steps)

    print(f"\nSparse graph (p={sparse_p}) active counts per step:")
    print([len(s) for s in history_sparse])

    print(f"\nDense graph (p={dense_p}) active counts per step:")
    print([len(s) for s in history_dense])

    print("\nInterpretation:")
    print("- Each list shows how many nodes are 'active' (infected/informed) at each time step.")
    print("- Typically, the denser graph allows faster and wider propagation.")


if __name__ == "__main__":
    demo_algorithms()
    demo_simulation()
