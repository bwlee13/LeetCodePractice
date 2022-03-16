from collections import deque
"""
provided with a temp record temperatureRecord(temp, time)
return maximum temp in last 24 hours
ex: input= [(24,0), (14,8), (21,16), (20,25)] output= [24, 24, 24, 21]
"""


def daily_max_temp(temp_record):
    queue = deque()
    res = []
    for i in range(len(temp_record)):
        while queue and queue[0][1] < (temp_record[i][1]-24):
            queue.popleft()
        while queue and queue[-1][0] < temp_record[i][0]:
            queue.pop()
        queue.append(temp_record[i])
        res.append(queue[0][0])
    return res


temps = [(24,0), (14,8), (21,16), (20,25)]
# print(daily_max_temp(temps))