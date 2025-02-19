def weakest_strong_link(strength):
    m = len(strength)   # number of rows
    n = len(strength[0])    # number of columns

    # initialize min_rows and max_cols
    min_rows = [0] * m  
    max_cols = [0] * n
  
    # find the minimum value in each row and store it in min_rows
    for i in range(m):
        cur_min = float("inf")
        for j in range(n):
            cur_min = min(cur_min, strength[i][j])
        min_rows[i] = cur_min

    # find the maximum value in each column and store it in max_cols
    for j in range(n):
        cur_max = float("-inf")
        for i in range(m):
            cur_max = max(cur_max, strength[i][j])
        max_cols[j] = cur_max
    
    # check if the minimum value in a row is equal to the maximum value in a column
    for i in range(m):
        for j in range(n):
            if strength[i][j] == max_cols[j] and strength[i][j] == min_rows[i]:
                return strength[i][j]   # return the value if it is the weakest strong link
    
    # return -1 if there is no weakest strong link
    return -1