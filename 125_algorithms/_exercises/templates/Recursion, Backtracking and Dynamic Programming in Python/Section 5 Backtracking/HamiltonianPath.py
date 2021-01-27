
class HamiltonianPath:

    ___ __init__(self, adjacency_matrix
        self.n = le_(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    ___ hamiltonian_path(self

        __ self.solve(1
            self.show_hamiltonian_path()
        ____
            print('There is no solution to the problem...')

    ___ solve(self, position

        # BASE CASE
        __ position == self.n:
            r_ True

        ___ vertex_index __ range(1, self.n
            __ self.is_feasible(vertex_index, position
                # we include vertex (with vertex_index) in the solution
                self.path.append(vertex_index)

                __ self.solve(position+1
                    r_ True

                # when we have to backtrack
                # we have to remove vertex_index from the result (path)
                self.path.pop()

        # if we have considered all the vertexes without a success
        r_ False

    ___ is_feasible(self, vertex, actual_position

        # check whether is there a connection between the nodes
        __ self.adjacency_matrix[self.path[actual_position-1]][vertex] == 0:
            r_ False

        # whether we have already included that given vertex in the result
        ___ i __ range(actual_position
            __ self.path[i] == vertex:
                r_ False

        r_ True

    ___ show_hamiltonian_path(self
        ___ v __ self.path:
            print(v)


__ __name__ == '__main__':

    m = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 0]]

    hamiltonian_path = HamiltonianPath(m)
    hamiltonian_path.hamiltonian_path()
