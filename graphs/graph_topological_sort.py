import traceback


def dfs(adj, used, order, x):
    used[x] = 1
    for v in adj[x]:
        if used[v] == 0:
            dfs(adj, used, order, v)

    used[x] = -1
    order.append(x)


def topological_sort(adj):  # recursive dfs with
    used = [0] * len(adj)
    order = []

    for x in range(len(adj)):
        if used[x] == 0:
            dfs(adj, used, order, x)

    order.reverse()
    topological_order = [num + 1 for num in order]

    return topological_order


def test_one():
    num_nodes = 4
    num_edges = 3
    data = [1, 2, 4, 1, 3, 1]
    adj = _generate_adj_matrix(data, num_nodes, num_edges)

    topological_order = topological_sort(adj)

    expected_order = [4, 3, 1, 2]

    assert topological_order == expected_order


def test_two():
    num_nodes = 4
    num_edges = 1
    data = [3, 1]
    adj = _generate_adj_matrix(data, num_nodes, num_edges)

    topological_order = topological_sort(adj)

    expected_order = [4, 3, 2, 1]

    assert topological_order == expected_order


def test_three():
    num_nodes = 5
    num_edges = 7
    data = [2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5, 3]
    adj = _generate_adj_matrix(data, num_nodes, num_edges)

    topological_order = topological_sort(adj)

    expected_order = [5, 4, 3, 2, 1]

    assert topological_order == expected_order


def _generate_adj_matrix(data, num_nodes, num_edges):
    edges = list(zip(data[0:(2 * num_edges):2], data[1:(2 * num_edges):2]))
    adj = [[] for _ in range(num_nodes)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    return adj


if __name__ == "__main__":
    try:
        print('begin tests')
        test_one()
        test_two()
        test_three()
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())

