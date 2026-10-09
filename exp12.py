# Depth Limited Search (DLS)

def dls(graph, current, goal, limit, path):

    # Add current node to path
    path.append(current)

    # Goal found
    if current == goal:
        return True

    # Depth limit reached
    if limit == 0:
        path.pop()
        return False

    # Visit neighboring nodes
    for neighbor in graph[current]:
        if neighbor not in path:
            if dls(graph, neighbor, goal, limit - 1, path):
                return True

    # Backtrack
    path.pop()
    return False


# Main Program
print("===== DEPTH LIMITED SEARCH =====")

n = int(input("Enter number of nodes: "))

graph = {}

# Create nodes
for i in range(n):
    graph[i] = []

# Enter edges
e = int(input("Enter number of edges: "))

print("Enter edges (source destination):")

for i in range(e):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# Starting node
start = int(input("Enter starting node: "))

# Goal node
goal = int(input("Enter goal node: "))

# Depth limit
limit = int(input("Enter depth limit: "))

path = []

# Perform DLS
found = dls(graph, start, goal, limit, path)

# Display result
if found:
    print("\nGoal Found!")
    print("Path:", " -> ".join(map(str, path)))
    print("Depth:", len(path) - 1)
else:
    print("\nGoal not found within the given depth limit.")


import heapq


# Uniform Cost Search (UCS)

def ucs(graph, start, goal):

    # Priority queue
    priority_queue = []

    # (cost, node, path)
    heapq.heappush(priority_queue, (0, start, [start]))

    # Store the lowest cost found for each node
    visited = {}

    while priority_queue:

        cost, current, path = heapq.heappop(priority_queue)

        # If node was already reached with lower cost
        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        # Goal found
        if current == goal:
            return path, cost

        # Explore neighbors
        for neighbor, edge_cost in graph[current]:

            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )

    return None, float('inf')


# Main Program

print("===== UNIFORM COST SEARCH =====")

n = int(input("Enter number of nodes: "))

graph = {}

# Create nodes
for i in range(n):
    graph[i] = []


# Enter edges
e = int(input("Enter number of edges: "))

print("Enter edges as:")
print("source destination cost")

for i in range(e):

    u, v, cost = map(int, input().split())

    graph[u].append((v, cost))
    graph[v].append((u, cost))


# Starting node
start = int(input("Enter starting node: "))

# Goal node
goal = int(input("Enter goal node: "))


# Perform UCS
path, cost = ucs(graph, start, goal)


# Display result
if path:

    print("\nGoal Found!")
    print("Optimal Path:", " -> ".join(map(str, path)))
    print("Minimum Cost:", cost)

else:

    print("\nGoal not found")