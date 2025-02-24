#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#

def numberOfWays(roads):
    # Construct an adjacency list to represent a graph
    n = max(max(x, y) for x, y in roads)
    graph = [[] for _ in range(n + 1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS calculates the distance between any two points
    def bfs(start):
        distances = [-1] * (n + 1)
        distances[start] = 0
        queue = [start]
        i = 0
        while i < len(queue):
            current = queue[i]
            i += 1
            for neighbor in graph[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances
    
    # Compute the distance between all pairs of points
    all_distances = [bfs(i) for i in range(1, n + 1)]
    
    # Check if the three points form an equal distance
    def check_equidistant(i, j, k):
        d1 = all_distances[i-1][j]
        d2 = all_distances[j-1][k]
        d3 = all_distances[i-1][k]
        return d1 == d2 and d2 == d3
    
    # Count all possible combinations of three points
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if check_equidistant(i, j, k):
                    count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    roads_rows = int(input().strip())
    roads_columns = int(input().strip())

    roads = []

    for _ in range(roads_rows):
        roads.append(list(map(int, input().rstrip().split())))

    result = numberOfWays(roads)

    fptr.write(str(result) + '\n')

    fptr.close()
