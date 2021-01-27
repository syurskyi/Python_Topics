
___ dijkstra(adjacency_matrix

    v = le_(adjacency_matrix)
    visited = [False ___ i __ range(v)]

    distance = [float('inf') ___ i __ range(v)]
    distance[0] = 0

    ___ i __ range(v-1

        min_vertex = find_min_vertex(distance, visited)
        visited[min_vertex] = True

        ___ j __ range(v
            __ adjacency_matrix[min_vertex][j] != 0 and not visited[j] :
                    new_dist = distance[min_vertex] + adjacency_matrix[min_vertex][j]
                    __ new_dist < distance[j]:
                        distance[j] = new_dist

    ___ i __ range(v
        print(i, ' ', distance[i])


___ find_min_vertex(distance, visited

    min_vertex = -1
    ___ i __ range(le_(distance)):
        __ (min_vertex == -1 or distance[min_vertex] > distance[i]) and not visited[i]:
            min_vertex = i
    r_ min_vertex


adjacency_matrix = [
    [0, 3, 5, 6, 0, 8, 0],
    [3, 0, 0, 4, 2, 0, 5],
    [5, 0, 0, 0, 0, 4, 0],
    [6, 4, 0, 0, 0, 1, 6],
    [0, 2, 0, 0, 0, 0, 10],
    [8, 0, 6, 1, 0, 0, 8],
    [0, 8, 0, 6, 10, 8, 0]
]

dijkstra(adjacency_matrix)
