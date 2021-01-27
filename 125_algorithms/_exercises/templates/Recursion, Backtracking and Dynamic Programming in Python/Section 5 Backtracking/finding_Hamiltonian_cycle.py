c_ HamiltonianProblem:

    ___  -   adjacency_matrix
        n = le_(adjacency_matrix)
        adjacency_matrix = adjacency_matrix
        hamiltonian_path = []

    ___ hamiltonian_cycle(self

        # we start with first vertex (index 0)
        hamiltonian_path.ap..(0)

        # first vertex is already inserted so let's start with index 1
        __ solve(1
            show_cycle()
        ____
            print('No feasible solution found...')

    ___ solve  position

        # check whether if we are done: the last node can be connected to the first in order to form a cycle?
        __ position __ n:

            last_item_index = hamiltonian_path[position - 1]

            # last node can be connected to the first one so return true because
            # we can form a cycle
            __ adjacency_matrix[last_item_index][0] __ 1:
                hamiltonian_path.ap..(0)
                print(hamiltonian_path)
                r_ T..
            # backtrack because we can not form a cycle
            ____
                r_ F..

        ___ vertex_index __ range(1, n
            __ is_feasible(vertex_index, position
                hamiltonian_path.ap..(vertex_index)
                print(hamiltonian_path)

                __ solve(position + 1
                    r_ T..

                # BACKTRACK
                hamiltonian_path.pop()

        r_ F..

    ___ is_feasible  vertex, actual_position

        # first criteria: whether the two nodes are connected?
        __ adjacency_matrix[hamiltonian_path[actual_position - 1]][vertex] __ 0:
            r_ F..

        # second criteria: whether we have already added this given node?
        ___ i __ range(actual_position
            __ hamiltonian_path[i] __ vertex:
                r_ F..

        r_ T..

    ___ show_cycle(self

        print('Hamiltonian cycle exists: \n')

        ___ v __ hamiltonian_path:
            print(v)


__ ___ __ "__main__":
    m = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 0]]

    hamiltonian = HamiltonianProblem(m)
    hamiltonian.hamiltonian_cycle()