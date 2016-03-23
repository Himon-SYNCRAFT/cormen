"""
Find Eulerian Tour

Write a function that takes in a graph represented as a list of tuples and return a list of nodes that you would follow on an Eulerian Tour.

For example, if the input graph was [(1, 2), (2, 3), (3, 1)] A possible Eulerian tour would be [1, 2, 3, 1]
"""


def build_tour(connections, current_v):
    eulerian_tour = []
    while True:
        try:
            next_v = connections[current_v].pop()
        except KeyError:
            break
        eulerian_tour.append(next_v)

        connections[next_v].remove(current_v)

        current_v = next_v

    return eulerian_tour


def find_eulerian_tour(graph):
    connections = {}
    eulerian_tour = []

    for vertex1, vertex2 in graph:
        try:
            connections[vertex1].add(vertex2)
        except KeyError:
            connections[vertex1] = set()
            connections[vertex1].add(vertex2)

        try:
            connections[vertex2].add(vertex1)
        except KeyError:
            connections[vertex2] = set()
            connections[vertex2].add(vertex1)

    current_v = next(iter(connections.keys()))
    eulerian_tour.append(current_v)

    eulerian_tour.extend(build_tour(connections, current_v))

    for index in range(len(eulerian_tour)):
        vertex = eulerian_tour[index]

        if len(connections[vertex]) > 0:
            tour = build_tour(connections, vertex)

            for item in tour:
                eulerian_tour.insert(index, item)

    return eulerian_tour


if __name__ == '__main__':
    assert find_eulerian_tour([(1, 2), (2, 3), (3, 1)]) == [1, 2, 3, 1]
    a = find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8),
                            (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])
    print(a)
