def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    for index in range(1, len(queries)):
        temp = sum(queries[0: index])
        waiting_time += temp
    return waiting_time
    
