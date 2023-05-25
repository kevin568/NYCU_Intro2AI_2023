import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def read_file(Map):
    with open(edgeFile, newline='') as csvfile:    #open csv file 
        Edge = csv.reader(csvfile, delimiter=',')
        jump = next(Edge) #jump the first 
        counter = 0 
        for row in Edge:
            vertex1, vertex2, distance_v1_v2, speed_limit = row
            vertex2 = int(vertex2)
            counter = counter + 1 
            vertex1 = int(vertex1)
            distance_v1_v2 = float(distance_v1_v2)
            Map[vertex1].append([vertex2, distance_v1_v2])

def read_file_speed(Map, maxSpped):

    with open(edgeFile, newline='') as csvfile:    #open csv file 
        Edge = csv.reader(csvfile, delimiter=',')
        jump = next(Edge) #jump the first 
        counter = 0 
        for row in Edge:
            vertex1, vertex2, distance_v1_v2, speed_limit = row
            vertex2 = int(vertex2)
            counter = counter + 1 
            vertex1 = int(vertex1)
            distance_v1_v2 = float(distance_v1_v2)
            speed_limit = float(speed_limit)
            maxSpped = max(maxSpped, speed_limit / 3.6)  #calculate the admissible heristic function 
            distance_v1_v2 = distance_v1_v2 / (speed_limit / 3.6)            
            Map[vertex1].append([vertex2, distance_v1_v2])            

    return maxSpped

def read_heristic_time(heristic_f,maxSpped,end):
    with open(heuristicFile, newline='') as csvfile: #open heristic_file 
        rows = csv.reader(csvfile, delimiter=',')
        counter = 0 
        infromation = next(rows)
        for i in range(1, 4):
            infromation[i] = int(infromation[i])
            counter = counter + 1 
        for row in rows:
            row[0] = int(row[0])
            counter = counter + 1 
            for i in range(1, 4):
                counter = counter + 1 
                if infromation[i] == end:
                    heristic_f[row[0]] = float(row[i]) / maxSpped #get into the admissible heristic function 

def read_heristic(heristic_f,end):
    with open(heuristicFile, newline='') as csvfile: ##open heristic_file 
        rows = csv.reader(csvfile, delimiter=',')
        counter = 0
        infromation = next(rows)
        for i in range(1, 4):
            counter = counter + 1 
            infromation[i] = int(infromation[i])
        for row in rows:
            counter = counter + 1 
            for i in range(1, 4):
                counter = counter + 1 
                if infromation[i] == end:
                    heristic_f[int(row[0])] = float(row[i]) #get heristic function 

                    