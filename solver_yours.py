#!/usr/bin/env python3
#beginning part from greedy

import sys
import math
import numpy as np

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)
    #path size,path
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    #xrange 
    def path_length(path):
        n = 0
        for i in range(1, len(path)):
            n += dist[path[i - 1]][path[i]]
        n += dist [path[0]][path[-1]]
        return n
    #2-opt optimization
    def opt_2(N):
        def opt_2(n, path):
                global min_len, min_path
                if N == n:
                    new_len = path_len(path)
                    if new_len < min_len:
                    min_len = new_len
                    min_path = path[:]

            else:
                for x in range(1, N):
                    if x not in path:
                        path.append(x)
                        opt_2_extra(n + 1, path)
                        path.pop()
            #nearest neighbor (easy greedy)
            global min_len, min_path
            min_len = 1e100
            min_path = []
            for x in range(1, N):
                path = [x,0]
                opt_2_extra(2, path)
            print (min_len)
            return min_path
        return opt_2(N)

    #
    '''
    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    return solution
    '''

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
