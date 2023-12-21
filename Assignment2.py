# CS4033 AI Assignment 2: A* Search
# Group 39 - Clair Grywalski, Andrew Pipo, Max Santos

import heapq
from collections import defaultdict, deque

# City connections and costs
graph = {
    "Arad": {
        "Zerind": 75,
        "Sibiu": 140,
        "Timisoara": 118
    },
    "Bucharest": {
        "Giurgiu": 90,
        "Urziceni": 85,
        "Fagaras": 211,
        "Pitesti": 101
    },
    "Craiova": {
        "Pitesti": 138,
        "Rimnicu Vilcea": 146,
        "Drobeta": 120
    },
    "Drobeta": {
        "Craiova": 120,
        "Mehadia": 75
    },
    "Eforie": {
        "Hirsova": 86
    },
    "Fagaras": {
        "Sibiu": 99,
        "Bucharest": 211
    },
    "Giurgiu": {
        "Bucharest": 90
    },
    "Hirsova": {
        "Eforie": 86,
        "Urziceni": 98
    },
    "Iasi": {
        "Neamt": 87,
        "Vaslui": 92
    },
    "Lugoj": {
        "Mehadia": 70,
        "Timisoara": 111
    },
    "Mehadia": {
        "Lugoj": 70,
        "Drobeta": 75
    },
    "Neamt": {
        "Iasi": 87
    },
    "Oradea": {
        "Zerind": 71,
        "Sibiu": 151
    },
    "Pitesti": {
        "Bucharest": 101,
        "Rimnicu Vilcea": 97,
        "Craiova": 138
    },
    "Rimnicu Vilcea": {
        "Sibiu": 80,
        "Pitesti": 97,
        "Craiova": 146
    },
    "Sibiu": {
        "Fagaras": 99,
        "Oradea": 151,
        "Arad": 140,
        "Rimnicu Vilcea": 80
    },
    "Timisoara": {
        "Lugoj": 111,
        "Arad": 118
    },
    "Urziceni": {
        "Hirsova": 98,
        "Vaslui": 142,
        "Bucharest": 85
    },
    "Vaslui": {
        "Iasi": 92,
        "Urziceni": 142
    },
    "Zerind": {
        "Oradea": 71,
        "Arad": 75
    }
}

# Straight-Line Values
heuristic = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


# Breadth First 
def breadthSearch(start, goal):
  # Initializes queue with starting city and visited with starting city, which tracks what nodes have been visited
  visited = set()
  queue = deque()
  visited.add(start)
  queue.append(start)

  # Values for tracking path and cost
  path = []
  cost = 0

  # Loops through the queue until the goal city is reached
  while queue:
    # Pops the left most node FIFO
    node = queue.popleft()
    path.append(node)

    # Checks for goal city, if true returns path and total cost
    if node == goal:
      #Code for counting the total cost based off the final path
      check = []
      for m in path:
        for neighbor, step_cost in graph[m].items():
          if neighbor in path and neighbor not in check:
            cost = cost + step_cost
            # Stores values already traveled to
            check.append(m)
            check.append(neighbor)
      return path, cost

    # Traverses the graph, visiting in the breadth first order
    for neighbor, step_cost in graph[node].items():
      if neighbor not in visited:
        # Adds current node to list of visited
        visited.add(neighbor)
        # Pushes node in queue
        queue.append(neighbor)

  # Returns empty path with no cost if path does not exist
  return [], 0

# Depth Search 
def depthSearch(start, goal):
  # initialize the queue with start city, path and visited set to blank/new
  visited = {start}
  queue, path = [], []

  # add the start city to the to the queue
  queue.append(start)

  # initialize the cost/mileage
  cost = 0

  while queue:  # runs while there is new content in the queue
    node = queue.pop() # pops the next node down from the queue
    path.append(node)  # add the node to the queue and path
    
    if node == goal: # if the node is the destination:
      check = []
      for i in path: # iterate through the path
        for neighbor, step_cost in graph[i].items():
          if neighbor in path and neighbor not in check:
            cost = cost + step_cost
            # Stores cost/values already traveled to
            check.append(i)
            check.append(neighbor)
      return path, cost

    for neighbor, step_cost in graph[node].items():  # loop through each neighbor
      if neighbor not in visited:  # checks if a neighbor has not been visited
        visited.add(neighbor)  # add the new neighbor to the visited city
        queue.append(neighbor)  # add the new neighbor to the queue

  return [], 0  # return array/list and mileage as empty if there is no valid paths 



# A* Algorithm 


def astar_search(start, goal):
  #  queue tuples
  queue = [(0 + heuristic[start], 0, start, [])]
  visited = set()

  while queue:
    _, cost, current, path = heapq.heappop(queue)
    if current == goal:
      # return path + cost once goal reached
      return path + [current], cost

    visited.add(current)
    for neighbor, step_cost in graph[current].items():
      if neighbor not in visited:
        new_cost = cost + step_cost
        heapq.heappush(queue, (new_cost + heuristic[neighbor], new_cost,
                               neighbor, path + [current]))

  return [], 0


# Paths (Here is where we run the test path for each starting city
# for each algo.)
def main():
  start_cities = ["Oradea", "Timisoara", "Neamt"]
  goal_city = "Bucharest"

  for start_city in start_cities:
    print(f"STARTING FROM {start_city}:\n")

    # Breadth First Search

    print("Breadth First Search:")
    breadth_search, breadth_cost = breadthSearch(start_city, goal_city)
    print(f"Path = {breadth_search}")
    print(f"Path = {breadth_cost}")
    print("\n**********************************************************\n")

    # Depth First Search
    print("Depth First Search:")
    depth_search, depth_cost = depthSearch(start_city, goal_city)
    print(f"Path = {depth_search}")
    print(f"Path = {depth_cost}")
    print("\n**********************************************************\n")

    # A* Search
    astar_path, astar_cost = astar_search(start_city, goal_city)
    print("A* Search:")
    print(f"Path = {astar_path}")
    print(f"Cost = {astar_cost}")
    print("**********************************************************\n")


# Run main function
if __name__ == "__main__":
  main()

# Discussion of correctness

# Breadth First
#The breadth first search algorithm explores the shallowest unexpanded node first, traversing as wide as possible before moving deeper. It will guarantee a valid path as long as the data you are searching is finite. In the run of this program, BFS does correctly reach Bucharest from the three test cities, although often it is not very efficient. This was the expected result of this algorithm.

# Depth First 
# The Depth First Search Algorithm is designed to explore the branch as far as possible before backtracking. It will guarantee a valid path, even though it may not be shortest path, although it fails in infinite-deep spaces. Based on the test cases, the algorithm was able to locate a valid path as expected to which in some cases it was the shortest and other cases it was not the shortest, which was as expected with the known behavior of this algorithm. This algorithm is accurate and appropiate for when finding any path that is valid is sufficient to the user, regardless of the distance/cost.

# A* Algorithm 
# The A* algorithm searches for the optimal path from a start to end city while simultaneously considering cost. This is done by the algorithm maintaining a priority queue and selecting a node with the lowest cost at each step. This process repeats until it reaches the goal city (or if it exhausts all possible paths). Correctness depends on the heuristic function, which estimates the cost to reach the goal from each node.

# Discussion of efficiency

# Breadth First
# In terms of efficiency, the breadth first search algorithm has a time complexity of O(b^d+1). The real challenge with this algorithm is space, as it keeps every node in memory (O(b^d+1)), and can easily generate nodes at 100MB/sec. In general it is not optimal, but can be if the cost is only 1 per step, or if the problem requires finding the shortest path or closest node, as this assignment does. In this program, BFS only just ended up being slightly more optimal than DFS when starting from Oradea, was worse when starting from Timisoara, and had the worst performance when starting from Neamt. BFS works most efficiently when the tree/data is shallow. The A* was significantly more efficient than BFS and DFS in most cases.

# Depth First 
# The Depth First Search Algorithm is designed to explore the branch as far as possible before backtracking. This means that while it finds paths that are not neccesairly the shortest, in certain cases, it could provide a direct path. The time complexity being O(b^d) at worst case in scenerios with deep tree structures certainly makes this not the most efficient. Additionally, using this algorithm, while using less memory, could lead to stack overflow errors/issues especially with deep tree structures.This algorithm could be optimized using memorization or pruning to prevent a redundency in node visits

# A* Algorithm 
# Depending on the heuristic function, O(b^d) is the time complexity of the A* search algorithm in a worst case. Because we need to track every node in a graph at the same time (including those unnecessary), we almost always have a time complexity of O(b^d). Additionally, because the heuristic function is using straight-line distance values, we have consistent and admissable performance. This also means that A* will never overestimate the cost to reach each goal since the heuristic is admissable.
# Compared the breadth search and depth search algorithms, A* has the potential to be more efficient as it searches the paths with lower costs first. This priority system enables it to find these optimal paths first.