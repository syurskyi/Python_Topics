
c_ HamiltonianPath:

    ___  -   adjacency_matrix
        n = le_(adjacency_matrix)
        adjacency_matrix = adjacency_matrix
        path = [0]

    ___ hamiltonian_path(self

        __ solve(1
            show_hamiltonian_path()
        ____
            print('There is no solution to the problem...')

    ___ solve  position

        # BASE CASE
        __ position __ n:
            r_ T..

        ___ vertex_index __ range(1, n
            __ is_feasible(vertex_index, position
                # we include vertex (with vertex_index) in the solution
                path.ap..(vertex_index)

                __ solve(position+1
                    r_ T..

                # when we have to backtrack
                # we have to remove vertex_index from the result (path)
                path.pop()

        # if we have considered all the vertexes without a success
        r_ F..

    ___ is_feasible  vertex, actual_position

        # check whether is there a connection between the nodes
        __ adjacency_matrix[path[actual_position-1]][vertex] __ 0:
            r_ F..

        # whether we have already included that given vertex in the result
        ___ i __ range(actual_position
            __ path[i] __ vertex:
                r_ F..

        r_ T..

    ___ show_hamiltonian_path(self
        ___ v __ path:
            print(v)


__ __name__ __ '__main__':

    m = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 0]]

    hamiltonian_path = HamiltonianPath(m)
    hamiltonian_path.hamiltonian_path()
