class HamiltonianProblem:

    ___ __init__(self, adjacency_matrix
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.hamiltonian_path = []

    ___ hamiltonian_cycle(self

        # we start with first vertex (index 0)
        self.hamiltonian_path.append(0)

        # first vertex is already inserted so let's start with index 1
        __ self.solve(1
            self.show_cycle()
        ____
            print('No feasible solution found...')

    ___ solve(self, position

        # check whether if we are done: the last node can be connected to the first in order to form a cycle?
        __ position == self.n:

            last_item_index = self.hamiltonian_path[position - 1]

            # last node can be connected to the first one so return true because
            # we can form a cycle
            __ self.adjacency_matrix[last_item_index][0] == 1:
                self.hamiltonian_path.append(0)
                print(self.hamiltonian_path)
                return True
            # backtrack because we can not form a cycle
            ____
                return False

        for vertex_index in range(1, self.n
            __ self.is_feasible(vertex_index, position
                self.hamiltonian_path.append(vertex_index)
                print(self.hamiltonian_path)

                __ self.solve(position + 1
                    return True

                # BACKTRACK
                self.hamiltonian_path.pop()

        return False

    ___ is_feasible(self, vertex, actual_position

        # first criteria: whether the two nodes are connected?
        __ self.adjacency_matrix[self.hamiltonian_path[actual_position - 1]][vertex] == 0:
            return False

        # second criteria: whether we have already added this given node?
        for i in range(actual_position
            __ self.hamiltonian_path[i] == vertex:
                return False

        return True

    ___ show_cycle(self

        print('Hamiltonian cycle exists: \n')

        for v in self.hamiltonian_path:
            print(v)


__ __name__ == "__main__":
    m = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

    hamiltonian = HamiltonianProblem(m)
    hamiltonian.hamiltonian_cycle()