import queue
import heapq
import traceback

__author__ = 'kclark'


def distance(adj, cost, s, t):
    dist = {s: 0}
    queue_dist = {}
    visited_set = set([s])

    priority_queue = queue.PriorityQueue(len(adj))
    for idx, v in enumerate(adj[s]):
        dist[v] = cost[s][idx]
        item = [dist[v], s, v]
        priority_queue.put(item)
        queue_dist[v] = item

    while not priority_queue.empty():
        vertex_cost, parent, vertex = priority_queue.get()

        if vertex in visited_set:
            continue

        visited_set.add(vertex)

        for idx, neighbor in enumerate(adj[vertex]):
            if neighbor in dist:
                if dist[neighbor] > dist[vertex] + cost[vertex][idx]:
                    dist[neighbor] = dist[vertex] + cost[vertex][idx]
                    queue_dist[neighbor][0] = dist[neighbor]
                    queue_dist[neighbor][1] = vertex
                    heapq._siftdown(priority_queue.queue, 0, priority_queue.queue.index(queue_dist[neighbor]))
            else:
                dist[neighbor] = cost[vertex][idx] + dist[vertex]
                item = [dist[neighbor], vertex, neighbor]
                priority_queue.put(item)
                queue_dist[neighbor] = item

    if t in dist:
        return dist[t]

    return -1


def _prepare_dependencies(data, n, m):
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1

    return adj, cost, s, t


def test_one():
    data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == 3


def test_two():
    data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4, 4, 1, 5]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == 6


def test_three():
    data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == -1


def test_four():
    data = [1, 0, 1, 1]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == 0


def test_five():
    data = [3, 2, 1, 2, 1, 2, 3, 2, 2, 3]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == 2


def test_six():
    data = [6, 10, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 5, 6, 2, 2, 5, 3, 3, 4, 4, 1, 6]
    n, m = data[0:2]
    data = data[2:]

    adj, cost, s, t = _prepare_dependencies(data, n, m)
    result = distance(adj, cost, s, t)

    assert result == 8


if __name__ == '__main__':
    try:
        print('begin tests')
        test_one()
        test_two()
        test_three()
        test_four()
        test_five()
        test_six()
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())
