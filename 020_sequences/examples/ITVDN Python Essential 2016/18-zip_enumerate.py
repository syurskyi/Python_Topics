# Встроенная функция zip возвращает объект-итератор, возвращающий
# кортежи, состоящие из соответствующих элементов заданных
# последовательностей. Количество элементов, которые возвращает
# итератор, равно длине наименьшей из последовательностей.

nodes = ['node1', 'node2', 'node3']
weights = [1, 7, 5, 5, 9, 3]

for node, weight in zip(nodes, weights):
    print('The weight of node', node, 'is', weight)

# Встроенная функция enumerate возвращает объект-итератор,
# возвращающий пары индексов и значений последовательности
# То есть, поведение enumerate(seq) аналогично
# zip(range(seq), seq))

for index, node in enumerate(nodes):
    print('nodes[{}] = {}'.format(index, node))
