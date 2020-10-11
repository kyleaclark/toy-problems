import traceback
import queue

__author__ = 'kclark'


def breadth_first_search(graph, root):
    dist = [-1 for _ in range(len(graph))]
    seen = set([root])
    queue_instance = queue.Queue(len(graph))
    queue_instance.put(root)
    dist[root] = 0

    while not queue_instance.empty():
        vertex = queue_instance.get()
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue_instance.put(neighbor)
                dist[neighbor] = dist[vertex] + 1

    return dist


def distance(adj, s, t):
    dist = breadth_first_search(adj, s)
    return dist[t]


def _prepare_dependencies(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    return adj, s, t


def test_one():
    data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4]
    adj, s, t = _prepare_dependencies(data)
    result = distance(adj, s, t)

    assert result == 2


def test_two():
    data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5]
    adj, s, t = _prepare_dependencies(data)
    result = distance(adj, s, t)

    assert result == -1


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