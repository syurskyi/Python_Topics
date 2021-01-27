
c_ ColoringProblem:

    ___  -   adjacency_matrix, num_colors
        n = le_(adjacency_matrix)
        adjacency_matrix = adjacency_matrix
        num_colors = num_colors
        colors = [0 ___ _ __ range(n)]

    ___ coloring_problem(self

        # we call the solve with first vertex (index 0)
        __ solve(0
            show_result()
        ____
            print('There is no feasible solution...')

    ___ solve  node_index

        __ node_index __ n:
            r_ T..

        # consider the colors
        ___ color_index __ range(1, num_colors+1
            __ is_color_valid(node_index, color_index
                colors[node_index] = color_index

                __ solve(node_index+1
                    r_ T..

                # BACKTRACKING
                # in this case backtracking means doing "nothing"

        r_ F..

    ___ is_color_valid  node_index, color_index

        # we have to check that the nodes are connected
        # AND we have to check that the given color is not shared
        # with these adjacent nodes
        ___ i __ range(n
            __ adjacency_matrix[node_index][i] __ 1 and color_index __ colors[i]:
                r_ F..

        r_ T..

    ___ show_result(self
        ___ v, c __ zip(range(n), colors
            print('Node %d has color value %d' % (v, c))


__ ___ __ '__main__':

    m = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

    problem = ColoringProblem(m, 3)
    problem.coloring_problem()
