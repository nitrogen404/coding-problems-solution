# O(N) space
# O(N) time
def tournamentWinner(competitions, results):
    scoresTable = {}
    for match in competitions:
        if match[0] not in scoresTable:
            scoresTable.update({match[0]: 0})
        if match[1] not in scoresTable:
            scoresTable.update({match[1]: 0})


    for idx in range(len(results)):
        if results[idx] == 0:
            scoresTable[competitions[idx][1]] += 3
            scoresTable[competitions[idx][0]] += 0
        elif results[idx] == 1:
            scoresTable[competitions[idx][0]] += 3
            scoresTable[competitions[idx][1]] += 0
            
    return max(scoresTable, key=scoresTable.get)
