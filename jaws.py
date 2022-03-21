from collections import deque


def perform(query):
    queue = deque([])
    out = []
    for q in query:
        if q[0] == 'INSERT':
            queue.appendleft(q[1])
        elif q[0] == 'SHIP':
            if len(queue) < 3:
                out.append(['NA'])
            else:
                to_ship = []
                to_ship.append(queue.pop())
                to_ship.append(queue.pop())
                to_ship.append(queue.pop())

                out.append(to_ship)

    return out

