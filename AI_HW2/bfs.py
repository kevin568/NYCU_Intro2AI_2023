from collections import defaultdict 
from read_file import read_file

Map = defaultdict(list)  


def bfs(start, end):
    vertex_go_through = 0  
    counter = 0 

    visited = set()     # use set to check the visited vertex 
    pre_distance = {}         # stored the pre_distance
    Q_temp = []        # the queue to store temp vertex information 
    
    read_file(Map) #read the file

    Q_temp.append(start) #add start into queue
    visited.add(start) # add start into visited set 

    iffind = False
    pre_distance[start] = start
    
    while len(Q_temp) > 0:    #perform bfs using queue 
        now = Q_temp[0]   #get the first element 
        Q_temp.remove(now) # pop it 
        counter = counter+1
        for v1, distancev1 in Map[now]:  #iterate map element and add them into queue also update information 
            if v1 not in visited:      
                vertex_go_through = vertex_go_through + 1 
                pre_distance[v1] = [now, distancev1] 
                Q_temp.append(v1)       
                visited.add(v1)
                counter = counter+1          

            
            if v1 == end:         #if find = break (solve)
                iffind = True
                break
        if iffind == True: #if find = break (solve)
            break
    
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
    return route, total_distance, vertex_go_through
            
    

if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
