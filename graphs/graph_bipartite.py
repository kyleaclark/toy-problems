import traceback
import queue

__author__ = 'kclark'


def bipartite(adj):
    src = 0
    colors = [-1] * len(adj)
    colors[src] = 1

    queue_instance = queue.Queue(len(adj))
    queue_instance.put(src)

    while not queue_instance.empty():
        vertex = queue_instance.get()
        for neighbor in adj[vertex]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - colors[vertex]
                queue_instance.put(neighbor)
            elif colors[neighbor] == colors[vertex]:
                return 0

    return 1


def _prepare_dependencies(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    return adj


def test_one():
    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    adj = _prepare_dependencies(data)
    result = bipartite(adj)

    assert result == 0


def test_two():
    data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4]
    adj = _prepare_dependencies(data)
    result = bipartite(adj)

    assert result == 1


if __name__ == '__main__':
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