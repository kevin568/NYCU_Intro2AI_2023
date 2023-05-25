from collections import defaultdict 
from read_file import read_file

Map = defaultdict(list)  


def ucs(start, end):
    counter = 0 

    visited = set()     # use set to check the visited vertex 
    pre_distance = {}         # stored the pre_distance
    Q_temp = []        # the queue to store temp vertex information 
       
    vertex_go_through = 0 

    read_file(Map) #read the file 
    Q_temp.append([start, 0.0, start, 0]) #add start into Q temp 
    pre_distance[start] = [start, 0.0] #add start into predistance 
    vertex_go_through = vertex_go_through + 1 #update information 

    while len(Q_temp) > 0: #iterate Q temp 
        weight_u = float("inf") #set infinite
        current_u = 0
        predistination_u = 0
        distance_u = 0.0
        counter = counter +1 

        for location, weight_i, pre_distination, distance_i in Q_temp:  #find the min weight 
            if weight_i < weight_u:
                weight_u = weight_i
                current_u = location
                predistination_u = pre_distination
                distance_u = distance_i
                counter = counter +1 
        
        Q_temp.remove([current_u, weight_u, predistination_u, distance_u]) #pop the min weight 

        if current_u in visited:   #we only go through the not visited 
            continue

        pre_distance[current_u] = [predistination_u, distance_u] # add it into predistance
        visited.add(current_u)          #add into visited set 

        if current_u == end:          #find answer
            break
        for current_i, distance_i in Map[current_u]: #iterate neigbor to find answer 
            if current_i not in visited:  
                Q_temp.append([current_i, distance_i + weight_u, current_u, distance_i])
                counter = counter +1 
        
        vertex_go_through = vertex_go_through + 1 

    
    total_distance = 0.0       #from 0.0 using float
    route = []          # the route 
    cur = end           #back search 

    while cur != start: #iterate the cur to get full route and information 
        next_vertex, distance = pre_distance[cur]
        route.append(int(cur))
        counter = counter +1 
        cur = next_vertex
        total_distance = total_distance + distance
    route.append(start)    
    return route, total_distance, vertex_go_through

if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
