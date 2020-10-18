import traceback

__author__ = 'kclark'


def relax(u, v, w, dist, prev):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        prev[v] = u


def negative_cycle(adj, cost):
    dist = [10000000] * len(adj)
    prev = [None] * len(adj)
    dist[0] = 0

    for i in range(len(adj) - 1):
        for u in range(len(adj)):
            for idx, v in enumerate(adj[u]):
                relax(u, v, cost[u][idx], dist, prev)

    # checks for negative cycles
    for u in range(len(adj)):
        for idx, v in enumerate(adj[u]):
            w = cost[u][idx]
            if dist[v] > dist[u] + w:
                return 1

    return 0


def _prepare_dependencies(data, n, m):
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    return adj, cost


def test_one():
    data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    n, m = data[0:2]
    data = data[2:]

    adj, cost = _prepare_dependencies(data, n, m)
    result = negative_cycle(adj, cost)

    assert result == 1


def test_two():
    data = [4, 4, 1, 2, -1, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    n, m = data[0:2]
    data = data[2:]

    adj, cost = _prepare_dependencies(data, n, m)
    result = negative_cycle(adj, cost)

    assert result == 0


def test_three():
    data = [1, 0, 1, 1]
    n, m = data[0:2]
    data = data[2:]

    adj, cost = _prepare_dependencies(data, n, m)
    result = negative_cycle(adj, cost)

    assert result == 0


def test_four():
    data = [3, 2, 1, 2, 1, 2, 3, 2, 2, 3]
    n, m = data[0:2]
    data = data[2:]

    adj, cost = _prepare_dependencies(data, n, m)
    result = negative_cycle(adj, cost)

    assert result == 0


def test_five():
    data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2]
    n, m = data[0:2]
    data = data[2:]

    adj, cost = _prepare_dependencies(data, n, m)
    result = negative_cycle(adj, cost)

    assert result == 0


if __name__ == '__main__':
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
