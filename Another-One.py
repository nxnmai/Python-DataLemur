def another_one(digits):
    # start with last index
    i = len(digits) - 1
    
    # convert all 9s to 0 from right to left
    while i >= 0 and digits[i] == 9:
        digits[i] = 0
        i -= 1
    
    # if there is a non-9 digit, increment it and return the array
    if i >= 0:
        digits[i] += 1
        return digits
  
    # if all digits are 9, add 1 to the front of the array
    return [1] + digits