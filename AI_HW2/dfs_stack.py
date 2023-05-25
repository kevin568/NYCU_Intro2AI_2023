from collections import defaultdict 
import csv
import sys
from read_file import read_file

edgeFile = 'edges.csv'

def dfs(start, end):
    Map = defaultdict(list) 
    visited = set()     # use set to check the visited vertex 
    pre_distance = {}         # stored the pre_distance
    counter = 0 
    vertex_go_through = 0        

    read_file(Map) #read_file
    stack = []
    stack = [(start,0.0)] #the stack to store information 

    while stack: #iterate stack 
        (v, distance) = stack.pop()
        if v == end:
            print('find end')
            break
            
        
        if v not in visited:
            visited.add(v) 
            vertex_go_through = vertex_go_through + 1 
            for u ,distance in Map[v]: #iterate neighbor and get information 
                if u not in visited:
                    
                    pre_distance[u] = [v, distance]
                    stack.append((u, distance)) #add vertex into stack 

    total_distance = 0.0       #from 0.0 using float
    route = []          # the route 
    cur = end           #back search 

    while cur != start: #iterate the cur to get full route and information 
        next_vertex, distance = pre_distance[cur]
        # print(total_distance)
        route.append(int(cur))
        counter = counter+1
        cur = next_vertex 
        total_distance = total_distance + distance
    route.append(start)    
    
    return route, total_distance , vertex_go_through


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')



