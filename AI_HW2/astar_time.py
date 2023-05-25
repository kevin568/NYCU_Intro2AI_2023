from collections import defaultdict 
from read_file import read_file_speed
from read_file import read_heristic_time


Map = defaultdict(list) 

"""
I use the highest limit speed in the real world as I want to calculate the time 
Because I use the highest limit speed to calculate time so h(n) will <= h*(n)
which is an admissible heuristic function
I implement the detail in read_heristic_time. 

"""


def astar_time(start, end):
    heristic_f = {}
    counter = 0 

    visited = set()     # use set to check the visited vertex 
    pre_distance = {}         # stored the pre_distance
    Q_temp = []        # the queue to store temp vertex information 
    
    maxSpped = 0.0
    maxSpped = read_file_speed(Map,maxSpped) #find the maxspeed and read the file 
    read_heristic_time(heristic_f,maxSpped,end) # get heristic_f

    pre_distance[start] = [start, 0.0] # add start into predistance

    Q_temp.append([start, heristic_f[start], start, 0])
    vertex_go_through = 0

    while len(Q_temp) > 0:
        weight_u = float("inf") #set infinite
        current_u = 0
        predistination_u = 0
        distance_u = 0.0
        counter = counter +1 

        for location, weight_i, pre_distination, distance_i in Q_temp: #find the smallest weight 
            if weight_i < weight_u:
                weight_u = weight_i
                current_u = location
                counter = counter +1
                predistination_u = pre_distination
                distance_u = distance_i
        
        Q_temp.remove([current_u, weight_u, predistination_u, distance_u]) #remove the smallest weight 

        if current_u in visited:
            continue
        weight_u = weight_u - heristic_f[current_u]  #update weight 

        pre_distance[current_u] = [predistination_u, distance_u] #update predistance 

        counter = counter +1
        visited.add(current_u) #add into visited set 
        vertex_go_through = vertex_go_through + 1 #update vettex go through 
        if current_u == end: 
            break
        for current_i, distance_i in Map[current_u]: #iterate add neighbor into Q_temp 
            if current_i not in visited:
                counter = counter +1
                Q_temp.append([current_i, distance_i + weight_u + heristic_f[current_i], current_u, distance_i])
    
    total_distance = 0.0       #from 0.0 using float
    route = []          # the route 
    cur = end           #back search 

    while cur != start: #iterate the cur to get full route and information 
        next_vertex, distance = pre_distance[cur]
        # print(total_distance)
        route.append(int(cur))
        cur = next_vertex
        total_distance = total_distance + distance
    route.append(start)    
    return route, total_distance, vertex_go_through



if __name__ == '__main__':
    path, time, num_visited = astar_time(426882161, 1737223506)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')