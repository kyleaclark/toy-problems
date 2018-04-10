import traceback


def dfs(adj, vertex, visited, order, component):
    visited[vertex] = component
    for u in adj[vertex]:
        if not visited[u]:
            dfs(adj, u, visited, order, component)

    order.append(vertex)


def number_of_strongly_connected_components(adj, adj_reversed):
    visited = [0] * len(adj_reversed)
    order = []
    num_connected = 0
    for vertex in range(len(adj_reversed)):
        if not visited[vertex]:
            num_connected += 1
            dfs(adj_reversed, vertex, visited, order, num_connected)

    num_connected = 0
    visited = [0] * len(adj)
    order.reverse()
    for vertex in order:
        if not visited[vertex]:
            num_connected += 1
            dfs(adj, vertex, visited, order, num_connected)

    return num_connected


def test_one():
    num_nodes = 4
    num_edges = 3
    data = [1, 2, 3, 2, 4, 3]
    adj, adj_reversed = _generate_adj_matrixes(data, num_nodes, num_edges)

    num_connected = number_of_strongly_connected_components(adj, adj_reversed)

    assert num_connected == 4


def test_two():
    num_nodes = 4
    num_edges = 4
    data = [1, 2, 4, 1, 2, 3, 3, 1]
    adj, adj_reversed = _generate_adj_matrixes(data, num_nodes, num_edges)

    num_connected = number_of_strongly_connected_components(adj, adj_reversed)

    assert num_connected == 2


def test_three():
    num_nodes = 5
    num_edges = 7
    data = [2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
    adj, adj_reversed = _generate_adj_matrixes(data, num_nodes, num_edges)

    num_connected = number_of_strongly_connected_components(adj, adj_reversed)

    assert num_connected == 5


def test_four():
    num_nodes = 100
    num_edges = 100
    data = [27, 96, 23, 51, 42, 10, 40, 22, 30, 41, 80, 40, 13, 70, 21, 94, 88, 35, 38, 86, 53, 83, 71, 84, 64, 26, 4, 46, 76, 43, 24, 76, 26, 83, 18, 75, 42, 98, 36, 39, 47, 63, 33, 96, 89, 54, 47, 80, 95, 8, 34, 41, 91, 45, 78, 1, 12, 74, 2, 37, 98, 81, 30, 32, 93, 30, 45, 71, 38, 44, 85, 18, 89, 10, 71, 35, 73, 52, 28, 42, 98, 20, 22, 69, 56, 79, 78, 63, 53, 58, 77, 13, 6, 11, 56, 36, 4, 11, 92, 63, 32, 78, 71, 24, 16, 79, 66, 89, 72, 6, 20, 15, 2, 91, 100, 75, 93, 7, 42, 100, 18, 88, 49, 75, 33, 78, 81, 1, 42, 95, 73, 64, 50, 66, 33, 68, 14, 38, 80, 89, 8, 16, 87, 18, 20, 80, 81, 38, 14, 35, 91, 20, 36, 5, 16, 8, 61, 11, 72, 91, 26, 57, 60, 83, 80, 11, 58, 1, 71, 36, 41, 30, 57, 46, 47, 82, 46, 74, 28, 9, 76, 70, 69, 58, 39, 73, 89, 55, 93, 54, 17, 92, 54, 44, 21, 69, 87, 58, 96, 34]

    adj, adj_reversed = _generate_adj_matrixes(data, num_nodes, num_edges)

    num_connected = number_of_strongly_connected_components(adj, adj_reversed)

    assert num_connected == 98


def _generate_adj_matrixes(data, num_nodes, num_edges):
    edges = list(zip(data[0:(2 * num_edges):2], data[1:(2 * num_edges):2]))
    adj = [[] for _ in range(num_nodes)]
    adj_reversed = [[] for _ in range(num_nodes)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_reversed[b - 1].append(a - 1)

    return adj, adj_reversed


if __name__ == "__main__":
    try:
        print('begin tests')
        test_one()
        test_two()
        test_three()
        test_four()
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())