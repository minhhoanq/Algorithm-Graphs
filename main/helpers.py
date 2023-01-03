import global_variables

def get_way(before_list, end):
    trace_list = [end]
    ver = end
    while True:
        ver = before_list[ver]
        if ver == None:
            break
        else:
            trace_list.insert(0, ver)
        #End if
    #End while
    trace_list = [str(x) for x in trace_list]
    return ' -> '.join(trace_list)
#End def

def isNegativeCycle(graph,dist):
    NUM = len(graph)
    for i in range(NUM):
        for j in range(NUM):
            if graph[j][i] != global_variables.NO_EDGE_VALUE and dist[j] != global_variables.MAX_EDGE_VALUE and dist[i] > dist[j] + graph[j][i]:
                return 1
    return 0

def isNegativeWeight(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if(graph[i][j] != global_variables.NO_EDGE_VALUE and graph[i][j] < 0):
                return 1
            #End if
        #End for
    #End for
    return 0
#End def