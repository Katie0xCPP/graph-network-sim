# Graph Algorithms and Network Propagation Simulation

This project implements essential graph algorithms (BFS, DFS, shortest paths, Dijkstra’s algorithm, PageRank-style random walks) and a simple network propagation simulator to study how connectivity influences spreading behavior. The codebase is written in Python and designed to run cleanly inside VS Code.

---

## Features

### Graph Algorithms
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Shortest paths in unweighted graphs (via BFS)
- Dijkstra’s algorithm for weighted graphs
- PageRank-style random walk with teleportation
- Random graph generator (Erdős–Rényi model)

### Network Propagation Simulation
- Simple diffusion model (infection or information spread)
- Adjustable initial active nodes
- Adjustable spread probability
- Adjustable number of simulation steps
- Comparison between sparse and dense network propagation

---

## Installation and Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd graph-network-sim
```

### 2. Optional: Create a virtual environment
```bash
python -m venv .venv
```

Activate it (Windows):
```bash
.venv\Scripts\Activate
```

### 3. Run the project
```bash
python main.py
```

---

## Project Structure

```
graph-network-sim/
│
├── graph_algorithms.py   # Graph class + BFS/DFS + Dijkstra + PageRank + generator
├── simulation.py         # Propagation model
├── main.py               # Demo and experiments
└── README.md
```

---

## Example Output (Simplified)

Algorithm demo:
```
BFS from A: ['A', 'B', 'C', 'D', 'E', 'F']
DFS from A: ['A', 'C', 'E', 'D', 'F', 'B']

Unweighted shortest-path distances:
A -> D: 2 edges

Weighted shortest-path distances (Dijkstra):
A -> F: 4.0
```

Propagation simulation:
```
Sparse graph active counts per step:
[1, 2, 3, 3, 3]

Dense graph active counts per step:
[1, 5, 12, 17, 20]
```

---

## Purpose

This project demonstrates practical understanding of:
- Graph data structures
- Classical graph algorithms
- Simulation-based analysis
- Connectivity-driven propagation behavior
- Clean multi-file Python project organization

---
