
def get_user_inputs():
    # 1. Take heuristic values
    heuristic = {}
    num_nodes = int(input("Enter total no of nodes: "))

    print("\nEnter heuristic value h(n) for each node:")
    for _ in range(num_nodes):
        node = input("Enter node name: ").strip().upper()
        h_val = float(input(f"Heuristic h({node}): "))
        heuristic[node] = h_val

    # 2. Take graph edges
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nEnter total number of directed edges: "))

    print("\nEnter edges in format (from_node to_node weight)")
    for i in range(num_edges):
        u, v, w = input(f"Edge {i + 1}: ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)

        if u in graph and v in heuristic:
            graph[u].append((v, weight))
        else:
            print("Invalid node. Please check the node names.")

    return graph, heuristic


def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select node with minimum f(n) = g(n) + h(n)
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )
        open_list.remove(current)

        current_node = current[0]

        # Check if goal is reached
        if current_node == goal:
            path = [current_node]

            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()
            return path, g_cost[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                came_from[neighbor] = current_node

                open_list.append((neighbor, new_cost))

    return None, float('inf')


# Main program
graph, heuristic = get_user_inputs()

start = input("\nEnter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid start or goal node.")
else:
    path, cost = astar(graph, heuristic, start, goal)

    if path:
        print("\nOptimal path:", " -> ".join(path))
        print("Minimum cost:", cost)
    else:
        print("No path found")
