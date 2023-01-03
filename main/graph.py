from global_variables import NO_EDGE_VALUE

def create_graphs():
    f = open('test_2_1.txt')
    #number of vertices
    nov = int(f.readline().strip())
    row = f.readlines()
    f.close()

    graph = [[NO_EDGE_VALUE for _ in range(nov)] for _ in range(nov)]

    for r in row:
        list_values = r.split()
        if len(list_values) != 3:
            continue
        else:
            r = int(list_values[0])
            c = int(list_values[1])
            d = int(list_values[2])
            graph[r][c] = d
        #End if
    #End for
    return graph
#End def