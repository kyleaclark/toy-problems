import traceback


def explore(adj, x, visited):
    if x not in visited:
        visited.append(x)
        return list(adj[x])

    return None


def number_of_components(adj):
    visited = []
    connected = 0

    for x in range(len(adj)):
        branch = explore(adj, x, visited)
        if branch:
            while branch:
                n = branch.pop(0)
                leaf = explore(adj, n, visited)
                if leaf:
                    branch.extend(leaf)

            connected += 1
        elif branch is not None:
            connected += 1

    return connected


def test_one():
    num_nodes = 4
    num_edges = 2
    data = [1, 2, 3, 2]
    adj = _generate_adj_x_y(data, num_nodes, num_edges)

    connected_components = number_of_components(adj)

    assert connected_components == 2


def test_two():
    num_nodes = 4
    num_edges = 3
    data = [1, 2, 3, 2, 4, 3]
    adj = _generate_adj_x_y(data, num_nodes, num_edges)

    connected_components = number_of_components(adj)

    assert connected_components == 1


def test_three():
    num_nodes = 4
    num_edges = 3
    data = [1, 2, 3, 2, 4, 3, 1, 4]
    adj = _generate_adj_x_y(data, num_nodes, num_edges)

    connected_components = number_of_components(adj)

    assert connected_components == 1


def test_four():
    num_nodes = 10
    num_edges = 20
    data = [5, 9, 4, 10, 2, 6, 5, 10, 6, 8, 2, 9, 4, 8, 4, 9, 2, 8, 3, 10, 6, 10, 2, 10, 1, 5, 3, 9, 1, 6, 7, 10, 1, 7, 1, 10, 2, 5, 3, 5, 7, 8]
    adj = _generate_adj_x_y(data, num_nodes, num_edges)

    connected_components = number_of_components(adj)

    assert connected_components == 1


def test_five():
    num_nodes = 100
    num_edges = 100
    data = [27, 96, 6, 9, 81, 98, 21, 94, 22, 68, 76, 100, 8, 50, 38, 86, 71, 75, 32, 93, 16, 50, 71, 84, 6, 72, 22, 58, 7, 19, 19, 76, 44, 75, 24, 76, 31, 35, 11, 89, 42, 98, 63, 92, 37, 38, 20, 98, 45, 91, 23, 53, 37, 91, 76, 93, 67, 90, 12, 22, 43, 52, 23, 56, 67, 68, 1, 21, 17, 83, 63, 72, 30, 32, 7, 91, 50, 69, 38, 44, 55, 89, 15, 23, 11, 72, 28, 42, 22, 69, 56, 79, 5, 83, 55, 73, 13, 72, 7, 93, 20, 54, 21, 55, 66, 89, 2, 91, 18, 88, 26, 64, 11, 61, 28, 59, 12, 86, 42, 95, 17, 82, 50, 66, 66, 99, 40, 71, 20, 40, 5, 66, 92, 95, 32, 46, 7, 36, 44, 94, 6, 31, 19, 67, 26, 57, 53, 84, 10, 68, 28, 74, 34, 94, 25, 61, 71, 88, 10, 89, 28, 52, 72, 79, 39, 73, 11, 80, 44, 79, 13, 77, 30, 96, 30, 53, 10, 39, 1, 90, 40, 91, 62, 71, 44, 54, 15, 17, 69, 74, 13, 67, 24, 69, 34, 96, 21, 50, 20, 91, 42, 46]
    adj = _generate_adj_x_y(data, num_nodes, num_edges)

    connected_components = number_of_components(adj)

    assert connected_components == 19


def _generate_adj_x_y(data, num_nodes, num_edges):
    edges = list(zip(data[0:(2 * num_edges):2], data[1:(2 * num_edges):2]))
    adj = [[] for _ in range(num_nodes)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    return adj


if __name__ == "__main__":
    try:
        print('begin tests')
        test_one()
        test_two()
        test_three()
        test_four()
        test_five()
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())