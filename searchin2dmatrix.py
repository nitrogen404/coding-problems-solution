target = int(input())
matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
          ]


def search(mat, tar):
    firstele = mat[0][0]
    lastrow = mat[len(mat) - 1]
    lastele = lastrow[len(lastrow) - 1]
    flag = False
    if tar in range(firstele, lastele + 1):
        for row in mat:
            if tar in row:
                flag = True
                break
            else:
                flag = False
        return flag

    else:
        return flag


print(search(matrix, target))
