import random
from typing import Iterable, Any, Set, List

from graph_algorithms import Graph


def simulate_propagation(
    graph: Graph,
    initial_active: Iterable[Any],
    p_spread: float,
    steps: int,
) -> List[Set[Any]]:
    """
    Simple propagation model:
    - Start with a set of 'active' (infected/informed) nodes.
    - At each step, each active node tries to activate its neighbors
      with probability p_spread.
    - Return a history list of sets (active nodes at each step).
    """
    active: Set[Any] = set(initial_active)
    history: List[Set[Any]] = [set(active)]

    for _ in range(steps):
        new_active = set(active)

        for node in list(active):
            for neighbor, _ in graph.adj.get(node, []):
                if neighbor not in active and random.random() < p_spread:
                    new_active.add(neighbor)

        history.append(set(new_active))

        # Stop early if nothing changes
        if new_active == active:
            break

        active = new_active

    return history
