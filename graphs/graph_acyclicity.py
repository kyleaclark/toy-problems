import traceback


def explore(adj, x, visited):
    if x in visited:
        return True

    if x not in visited:
        visited.append(x)
        return list(adj[x])

    return None


def acyclic(adj):
    for x in range(len(adj)):
        branch = adj[x]
        if isinstance(branch, list) and len(branch):
            for y in branch:
                visited = []
                source = []
                n = y
                while True:
                    leaf = explore(adj, n, visited)
                    if isinstance(leaf, list):
                        source.extend(leaf)

                    if len(source):
                        n = source.pop(0)
                    else:
                        break

                    if n == y:
                        has_cycle = 1
                        return has_cycle



    return 0


def test_one():
    num_nodes = 4
    num_edges = 4
    data = [1, 2, 4, 1, 2, 3, 3, 1]
    adj = _generate_adj_matrix(data, num_nodes, num_edges)

    is_acyclic = acyclic(adj)

    assert is_acyclic == 1


def test_two():
    num_nodes = 5
    num_edges = 7
    data = [1, 2, 2, 3, 1, 3, 3, 4, 1, 4, 2, 5, 3, 5]
    adj = _generate_adj_matrix(data, num_nodes, num_edges)

    is_acyclic = acyclic(adj)

    assert is_acyclic == 0


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
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())