import helpers
import global_variables

def dijkstra(graph, start, end):
    nov = len(graph)

    dist = [global_variables.MAX_EDGE_VALUE for _ in range(nov)]
    dist[start] = 0

    before_list = [start for _ in range(nov)]
    before_list[start] = None
    free = [True for _ in range(nov)]

    while 1:
        d = global_variables.MAX_EDGE_VALUE
        u = -1
        for i in range(nov):
            if free[i] and dist[i] < d:
                d = dist[i]
                u = i
        if u == -1 or u == end: break
        free[u] = 0
        for i in range(nov):
            w = graph[u][i]
            if free[i] and w != global_variables.NO_EDGE_VALUE and dist[i] > d + w:
                dist[i] = d + w
                before_list[i] = u
    
    if dist[end] == global_variables.MAX_EDGE_VALUE:
        print("Can't find the way.")
        return
    
    print(f'path from {start} to {end}')
    way = helpers.get_way(before_list, end)
    noti = f'{start} to {end} : ' + way + ' : ' + str(dist[end])
    print(noti)
#End def

def bellman_ford(graph, start, end):
    nov = len(graph)
    dist = [0 for _ in range(nov)]

    for i in range(nov):
        if graph[start][i] == global_variables.NO_EDGE_VALUE:
            dist[i] = global_variables.MAX_EDGE_VALUE
        else:
            dist[i] = graph[start][i]
    dist[start] = 0

    before_list = [start for _ in range(nov)]
    before_list[start] = None

    for i in range(nov-1):
        stop = 1
        for x in range(nov):
            if x == start:
                continue
            else:
                for y in range(nov):
                    if x == y: continue
                    if graph[x][y] != global_variables.NO_EDGE_VALUE and dist[y] > dist[x] + graph[x][y] and dist[y] != global_variables.NO_EDGE_VALUE:
                        dist[y] = dist[x] + graph[x][y]
                        before_list[y] = x
                        stop = 0
                    #End if
                #End for
            #End if
        #End for
        if stop == 1:
            break
    #End for
    
    if helpers.isNegativeCycle(graph,dist) == 1:
        print('Negative cycle.')
        return
    if dist[end] == global_variables.MAX_EDGE_VALUE:
        print("Can't find the way.")
        return
    print(f'Path from {start} to {end}')
    way = helpers.get_way(before_list, end)
    noti = f'{start} to {end} : ' + way + ' : ' + str(dist[end])
    print(noti)
#End def

def Floyd(graph):
    nov = len(graph)
    dist = [[0 for _ in range(nov)] for _ in range(nov)]
    for i in range(nov):
        for j in range(nov):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != global_variables.NO_EDGE_VALUE:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = global_variables.MAX_EDGE_VALUE
    for k in range(nov):
        for i in range(nov):
            for j in range(nov):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # print(dist, end = '\n')
    for rows in range(nov):
        print(dist[rows])