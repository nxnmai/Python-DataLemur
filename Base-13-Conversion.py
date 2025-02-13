def convertToBase13(num):
    digits = "0123456789ABC"
    ans = ""
    positive_num = abs(num)
  
    if num == 0:
        return "0"

    while positive_num > 0:
        ans += digits[int(positive_num % 13)]
        positive_num = int(positive_num / 13)

    if num < 0:
        return "-" + ans[::-1]
    return ans[::-1]