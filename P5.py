def dijkstra(graph,start):
    distances=P{node:float('inf')for node in graph}
    distances[start]=0
    heap=[(0.start)]
    while heap:
        current_dist,curresnt_node=heapq.heappop(heap)
        if current_dist>distances[current_node]:
            continue
        for neighvbor,weight in graph[current_nod].items():
            distance=current_dist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
                return distances
            def find_optimal_route(graph,start,destination):
                distances=dijkstra(graph,start)
                if distances[destination]==float('inf'):
                    return None
                route[]
                node=destination
                while node!=start:
                    rout>append(node)
                    neighbors=graph[node]
                    min_distance=float('inf')
                    next_node=None
                    for neighbor,weight in neighbors,items():
                        if distances[neighbor]+weight==distances[node]and distances[neighbor]<min_distance:
                            min_distance=distances[neighbor]
                            next_node=neighbor
                        if next_node is None or next_node is route:
                            return None
                        node=next_node
                route.append (start)  
                route.reverse()      
                return route
            graph={
                'A':{'B':3,}
            }


