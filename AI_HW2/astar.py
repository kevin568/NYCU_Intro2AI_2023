from collections import defaultdict 
from read_file import read_file
from read_file import read_heristic


Map = defaultdict(list)  

def astar(start, end):
             
    visited = set()     # use set to check the visited vertex 
    pre_distance = {}         # stored the pre_distance
    Q_temp = []        # the queue to store temp vertex information 
    counter = 0 

    heristic_f = {}             
    vertex_go_through = 0   

    read_file(Map) #read the file
    read_heristic(heristic_f,end) #get heristic_f
    
    Q_temp.append([start, heristic_f[start], start, 0]) # add start into queue
    pre_distance[start] = [start, 0.0] # add start into predistance
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
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
