import graph
import algorithm
import helpers

def main():
    gr = graph.create_graphs()
    if gr == None: return
    nov = len(gr)

    while(1):
        print('-------------------------------------------------------------------------')
        print('Select options (0,1 or 2) :')
        print('1. Find the shortest path between two vertices(Dijkstra or Bellman-Ford).')
        print('2. AlgorithmFloyd.')
        print('0. Exit!')
        s = int(input('Enter option : '))
        while(s != 0 and s != 1 and s != 2):
            s = int(input('Enter again, Please : '))
        if(s == 1):
            start = int(input('Enter start : '))
            end = int(input('Enter end : '))
            while(start > nov or end > nov):
                start = int(input('Enter start again : '))
                end = int(input('Enter end again : '))
            if start in range(nov) and end in range(nov):
                if(helpers.isNegativeWeight(gr)):
                    print('Algorithm BellMan Ford --->')
                    algorithm.bellman_ford(gr, start, end)
                else:
                    print('Algorithm Dijkstra ---->')
                    algorithm.dijkstra(gr, start, end)
            #End if
        #End if
        elif(s == 2): 
            print('Algorithm Floyd ---->')
            algorithm.Floyd(gr)
        #End elif
        else: 
            print('Exit.')
            break
        #End else
    #End while
#End def

if __name__ == '__main__':
    main()
#End if