def is_same_stripes(matrix):
    # get the matrix dimensions - m: rows, n: columns
    m, n = len(matrix), len(matrix[0])
  
    # iterate through the matrix (but exclude the first row and column)
    # because they don't have previous diagonal elements to compare with
    for i in range(1, m):
        for j in range(1, n):
            # check if the current element is not under bounds
            if i - 1 >= 0 and j - 1 >= 0:
                # compare current element with the previous diagonal element
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    #if they are not the same, return false immediately
                    return False
    # if all diagonals match and are valid, return true 
    return True