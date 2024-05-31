#!/usr/bin/env python3
import heapq

def find_minimum_latency_path(graph, compression_nodes, source, destination):
    # Initialize distances to infinity for all nodes
    distances = {node: float('inf') for node in graph}
    distances[source] = 0  # Distance from source to itself is 0

    # Priority queue to track the next nodes to explore
    priority_queue = [(0, source)]  # (distance, node)

    # Dijkstra's algorithm
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we have already found a shorter path to the current node, skip it
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, latency in graph[current_node]:
            # Apply compression if the neighbor is a compression node
            if neighbor in compression_nodes:
                latency = min(latency, 1)  # Example compression logic

            # Calculate the total latency from source to the neighbor
            total_latency = current_distance + latency

            # If this path is shorter than the known path to the neighbor, update the distance
            if total_latency < distances[neighbor]:
                distances[neighbor] = total_latency
                heapq.heappush(priority_queue, (total_latency, neighbor))

    # If destination is unreachable, return an error message
    if distances[destination] == float('inf'):
        print("Destination is unreachable!")
        return None

    # Otherwise, return the minimum total latency
    return distances[destination]

# Example usage 1
print("Example usage 1:")
graph = {
    'A': [('B', 10), ('C', 20)],
    'B': [('D', 15)],
    'C': [('D', 30)],
    'D': []
}
compression_nodes = ['B', 'C']
source = 'A'
destination = 'D'
min_latency = find_minimum_latency_path(graph, compression_nodes, source, destination)
print(f"Minimum total latency: {min_latency}")

# Example usage 2 when destination is unreachable
print("\nExample usage 2:")
graph = {
    'A': [('B', 900), ('C', 50)],
    'B': [('C', 600)],
    'C': [('D', 3)],
    'D': [('E', 100)],
    'E': [('D', 1000)],
    'F': [],  # Unreachable node
    'G': []
}
compression_nodes = ['C']
source = 'G'
destination = 'A'
min_latency = find_minimum_latency_path(graph, compression_nodes, source, destination)
if min_latency is not None:
    print(f"Minimum total latency: {min_latency}")
